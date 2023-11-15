var apiClient = apigClientFactory.newClient({ apiKey: "LyWiTzRIh88oMC765Wyy85QSxkJSAKwZ8e6O6wk4" });

function searchPhotos(){
    event.preventDefault();
    search_text = document.getElementById('search-bar').value;
    if (search_text){
        console.log("search_text = "+search_text)

		// Search for photos using API
        var params = {"q" : search_text};
        var album = document.getElementById("photos");

        apiClient.searchGet(params, {}, {}).then((response) => {
			console.log("response!")
			console.log(response);

			album.innerHTML = ""
			var results = response.data.results;
			console.log("result length")
			console.log(results)

			if (!results.length) {
				album.innerHTML += "No results";
			}
			else {
				// Process photos retrieved
				for(var i in results){
					console.log("process photo " + i);
					console.log(results[i])
					var photo_container = document.createElement("div");
					photo_container.className = "photo_container";
					photo_container.id = "photo" + i;

					var img = document.createElement('img');
                    img.src = results[i]['url'];
                    console.log(results[i]['url'])

					document.getElementById("photos").appendChild(photo_container);
					document.getElementById(photo_container.id).appendChild(img)
				}
			}
			document.getElementById('search-bar'.value) = "";
        });
    }else{
        document.getElementById("notification").innerHTML = "Please input search keywords";
    }
}