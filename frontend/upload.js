var apiClient = apigClientFactory.newClient({ apiKey: "LyWiTzRIh88oMC765Wyy85QSxkJSAKwZ8e6O6wk4" });

function convert64(file) {
    return new Promise((resolve, reject) => {
		// Read file content
        const fileReader = new FileReader();
		fileReader.readAsDataURL(file);

		// Extract base64 data if reading is successful
        fileReader.onload = () => {
            let base64Data = fileReader.result.replace(/^data:(.*;base64,)?/, '');
			// Ensure valid length
            if (base64Data.length % 4 > 0) {
                base64Data += '='.repeat(4 - (base64Data.length % 4));
            }
            resolve(base64Data);
        };

        fileReader.onerror = error => reject(error);
    });
  }

async function uploadPhotos(){
    event.preventDefault();
    var img = document.getElementById('img').files[0];
	var customLabelInput = document.getElementById('custom-labels');
	var customLabel = customLabelInput.value.trim().toLowerCase();

    if (img) {
        var msg = "";
		// Convert to base64
        var img_base64 = await convert64(img);

		// Send upload request
		// Do we upload as text/base64??
		var params = {"object" : img.name, "bucket" : "hw2-intelligent-photo-album", "Content-Type" : img.type, 'x-amz-meta-customLabels': customLabel};
		var response = await apiClient.uploadBucketObjectPut(params, img_base64, {})
		console.log(response)

		// Process response
		console.log(response);
		if (response.status === 200) {
			text = "Upload Successful!";
		} else if (response.status >= 400 && response.status < 500) {
			text = "Upload Failed (Client Error: " + response.statusText + ")";
		} else if (response.status >= 500 && response.status < 600) {
			text = "Upload Failed (Server Error: " + response.statusText + ")";
		} else {
			text = "Upload Failed";
		}
    }
	else {
        msg = "Please upload an image";
    }
    document.getElementById('img').value = "";
    document.getElementById("notification").innerHTML = msg;
}