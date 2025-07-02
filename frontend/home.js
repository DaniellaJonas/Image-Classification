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
  img.style.display = "block";

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
      return response.json();
    })
    .then(data => {
      const resultDiv = document.getElementById("result");
      resultDiv.textContent = "Prediction: " + data.result;
    })
    .catch(error => {
      console.error("Error:", error);
      const resultDiv = document.getElementById("result");
      resultDiv.textContent = "Something went wrong: " + error.message;
    });
}
