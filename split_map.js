const fs = require('fs');
const path = require('path');

const srcPath = path.join(__dirname, 'GeoAI_3D_Map.html');
const cssPath = path.join(__dirname, 'GeoAI_3D_Map.css');
const jsPath = path.join(__dirname, 'GeoAI_3D_Map.bundle.js');

try {
    console.log('Reading ' + srcPath + '...');
    let html = fs.readFileSync(srcPath, 'utf-8');

    // 1. Remove Mapbox secret token if present (replaces it with a dummy string)
    console.log('Scanning for Mapbox secret tokens...');
    // regex for the token is safe because it's a fixed-length exact match
    html = html.replace(/sk\.[a-zA-Z0-9_\-]{30,}/g, 'pk.REMOVED_SECRET_TOKEN');

    console.log('Extracting CSS styles...');
    const cssBlocks = [];
    let startIdx = 0;
    while ((startIdx = html.indexOf('<style>', startIdx)) !== -1) {
        let endIdx = html.indexOf('</style>', startIdx);
        if (endIdx === -1) break;
        // get inner content
        cssBlocks.push(html.substring(startIdx + 7, endIdx));
        startIdx = endIdx + 8;
    }

    console.log('Extracting inline JS scripts...');
    const jsBlocks = [];
    startIdx = 0;
    while ((startIdx = html.indexOf('<script>', startIdx)) !== -1) {
        let endIdx = html.indexOf('</script>', startIdx);
        if (endIdx === -1) break;
        // get inner content
        jsBlocks.push(html.substring(startIdx + 8, endIdx));
        startIdx = endIdx + 9;
    }

    console.log('Cleaning up HTML...');
    // We use split-join to reliably remove exact blocks without regex
    // For CSS
    while ((startIdx = html.indexOf('<style>')) !== -1) {
        let endIdx = html.indexOf('</style>', startIdx);
        if (endIdx === -1) break;
        html = html.substring(0, startIdx) + html.substring(endIdx + 8);
    }
    
    // For JS
    while ((startIdx = html.indexOf('<script>')) !== -1) {
        let endIdx = html.indexOf('</script>', startIdx);
        if (endIdx === -1) break;
        html = html.substring(0, startIdx) + html.substring(endIdx + 9);
    }

    // 4. Inject links back into HTML
    console.log('Injecting CSS/JS links...');
    const headInjection = '\n    <link rel="stylesheet" href="GeoAI_3D_Map.css">\n';
    const bodyInjection = '\n    <script src="GeoAI_3D_Map.bundle.js"></script>\n';
    
    html = html.replace('</head>', headInjection + '</head>');
    html = html.replace('</body>', bodyInjection + '</body>');

    // 5. Write the outputs
    console.log('Writing CSS file (' + cssBlocks.length + ' blocks)...');
    fs.writeFileSync(cssPath, cssBlocks.join('\n\n'), 'utf-8');

    console.log('Writing JS bundle (' + jsBlocks.length + ' blocks)...');
    fs.writeFileSync(jsPath, jsBlocks.join('\n\n'), 'utf-8');

    console.log('Updating HTML file...');
    fs.writeFileSync(srcPath, html, 'utf-8');

    console.log('Successfully completed! The file is now clean and split.');
} catch (err) {
    console.error('Error occurred:', err);
}
