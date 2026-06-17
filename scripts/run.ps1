param (
    [string]$Mode = "dev"
)

if ($Mode -eq "test") {
    Write-Host "Ejecutando en modo TEST..."
    docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
} else {
    Write-Host "Ejecutando en modo DESARROLLO..."
    docker-compose up -d
    Write-Host "Aplicación iniciada en http://localhost:5000"
}
