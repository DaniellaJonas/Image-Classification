function upload() {
    document.getElementById('fileInput').click();
}

function img_load(event) {
    const file = event.target.files[0];

    if (!file || (file.type !== "image/jpeg" && file.type !== "image/png")) {
        alert("Please upload a PNG or JPG image.");
        return;
    }

    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(file);

    img.onload = () => {
        URL.revokeObjectURL(img.src);
        img.style.display = "block";
    };

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:5000/predict", { 
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP status " + response.status);
        }
        return response.text();
    })
    .then(data => {
        alert("Prediction: " + data);
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong: " + error.message);
    });
}
