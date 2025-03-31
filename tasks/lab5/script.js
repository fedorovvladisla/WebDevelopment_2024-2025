function changeImage() {
    let img = document.getElementById("mainImage");
    if (img.src.includes("image1.jpg")) {
        img.src = "images/image2.jpg";
    } else {
        img.src = "images/image1.jpg";
    }
}

function showTooltip(event, text) {
    const tooltip = document.getElementById("tooltip");
    tooltip.textContent = text;
    tooltip.style.display = "block";
    tooltip.style.left = (event.pageX + 10) + 'px';
    tooltip.style.top = (event.pageY + 10) + 'px';
}

function hideTooltip() {
    document.getElementById("tooltip").style.display = "none";
}
