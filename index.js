async function checkSpam() {

    let text =
    document.getElementById("message").value;

    if(text === ""){

        alert("Enter email text");

        return;
    }

    let loading =
    document.getElementById("loading");

    loading.style.display = "block";

    try {

        const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        });

        const data =
        await response.json();

        document.getElementById("result")
        .innerHTML = data.result;

        document.getElementById("percentage")
        .innerHTML =
        "Threat Level : " +
        data.score + "%";

        document.getElementById("detectedWords")
        .innerHTML =
        "Detected Words : " +
        data.detected_words.join(", ");

        if(data.result === "SPAM"){

            document.getElementById("result")
            .style.color = "red";
        }
        else{

            document.getElementById("result")
            .style.color = "lime";
        }

    }
    catch(error){

        alert(
        "Cannot connect to backend");

        console.log(error);
    }

    loading.style.display = "none";
}