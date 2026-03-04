<?php
// Mendapatkan nama host (misal: desa-maju.localhost)
$host_akses = $_SERVER['HTTP_HOST'];

// Pecah stringnya untuk ambil nama desanya saja
$subdomain = explode('.', $host_akses)[0];

if ($subdomain == 'localhost' || $subdomain == 'www') {
    echo "<h1>Halaman Utama Portal Pusat</h1>";
    echo "<p>Silakan akses subdomain desa masing-masing.</p>";
    exit;
}

// Sekarang gunakan $subdomain ini untuk query ke database!
echo "<h1>Selamat Datang di Portal: " . strtoupper($subdomain) . "</h1>";

// Query ke database cari desa yang namanya sesuai $subdomain
// $stmt = $pdo->prepare("SELECT * FROM desa WHERE slug = ?");
// $stmt->execute([$subdomain]);
?>
