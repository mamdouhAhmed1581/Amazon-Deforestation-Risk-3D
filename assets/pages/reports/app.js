function exportData(format) {
            const data = {
                type: "FeatureCollection",
                features: [
                    { type: "Feature", properties: { risk: 0.87, zone: "High", region: "Rondônia" }, geometry: { type: "Point", coordinates: [-62.5, -10.2] } },
                    { type: "Feature", properties: { risk: 0.72, zone: "High", region: "Pará" }, geometry: { type: "Point", coordinates: [-55.3, -6.8] } },
                    { type: "Feature", properties: { risk: 0.45, zone: "Medium", region: "Amazonas" }, geometry: { type: "Point", coordinates: [-60.1, -3.5] } }
                ]
            };

            let content, filename, type;
            if (format === 'geojson') {
                content = JSON.stringify(data, null, 2);
                filename = 'risk_zones_2026.geojson';
                type = 'application/json';
            } else if (format === 'csv') {
                content = 'longitude,latitude,risk,zone,region\n';
                data.features.forEach(f => {
                    content += `${f.geometry.coordinates[0]},${f.geometry.coordinates[1]},${f.properties.risk},${f.properties.zone},${f.properties.region}\n`;
                });
                filename = 'analysis_data.csv';
                type = 'text/csv';
            } else if (format === 'png') {
                alert('📸 Risk map screenshot will be exported as PNG');
                return;
            }

            const blob = new Blob([content], { type });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            a.click();
            URL.revokeObjectURL(url);
        }

        function generatePDF() {
            const element = document.getElementById('reportPreview');
            const actionBar = element.querySelector('.action-bar');
            if (actionBar) actionBar.style.display = 'none';

            const opt = {
                margin: 0.5,
                filename: 'GeoAI_Deforestation_Report.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2, useCORS: true, backgroundColor: '#070b13' },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };

            html2pdf().set(opt).from(element).save().then(() => {
                if (actionBar) actionBar.style.display = 'flex';
            });
        }

        function shouldAutoGenerateReport() {
            const params = new URLSearchParams(window.location.search);
            return params.get('action') === 'generate';
        }

        // Hide loading
        window.addEventListener('load', () => {
            setTimeout(() => {
                const overlay = document.getElementById('loadingOverlay');
                if (overlay) overlay.classList.add('fade-out');
            }, 600);

            if (shouldAutoGenerateReport()) {
                if (window.history && typeof window.history.replaceState === 'function') {
                    window.history.replaceState(null, '', window.location.pathname + window.location.hash);
                }

                setTimeout(() => {
                    generatePDF();
                }, 1200);
            }
        });


