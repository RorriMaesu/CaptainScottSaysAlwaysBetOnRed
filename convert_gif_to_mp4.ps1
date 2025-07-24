# PowerShell script to convert CaptainScottathyRichAnimation2.gif to CaptainScottathyRichAnimation2.mp4 using ffmpeg
# Requires ffmpeg to be installed and available in PATH

$gif = "CaptainScottathyRichAnimation2.gif"
$mp4 = "CaptainScottathyRichAnimation2.mp4"

if (-Not (Test-Path $gif)) {
    Write-Host "GIF file not found: $gif"
    exit 1
}

# Convert GIF to MP4
ffmpeg -y -i $gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" $mp4

if (Test-Path $mp4) {
    Write-Host "Successfully created $mp4"
} else {
    Write-Host "Failed to create $mp4"
}
