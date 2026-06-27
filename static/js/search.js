const searchInput = document.getElementById("globalSearch");
const resultsBox = document.getElementById("searchResults");

if (searchInput && resultsBox) {

    searchInput.addEventListener("keyup", async function () {

        const q = this.value.trim();

        if (q.length < 2) {
            resultsBox.style.display = "none";
            resultsBox.querySelector(".list-group").innerHTML = "";
            return;
        }

        try {

            const response = await fetch(`/zoeken?q=${encodeURIComponent(q)}`);
            const data = await response.json();

            let html = "";

            // Klanten
            if (data.klanten.length > 0) {

                html += `
                    <div class="list-group-item active">
                        <i class="bi bi-people"></i>
                        Klanten
                    </div>
                `;

                data.klanten.forEach(klant => {

                    html += `
                        <a href="/klanten/${klant.id}"
                           class="list-group-item list-group-item-action">

                            👤 ${klant.naam}

                        </a>
                    `;

                });

            }

            // Projecten
            if (data.projecten.length > 0) {

                html += `
                    <div class="list-group-item active">
                        <i class="bi bi-folder2-open"></i>
                        Projecten
                    </div>
                `;

                data.projecten.forEach(project => {

                    html += `
                        <a href="/project/${project.id}"
                           class="list-group-item list-group-item-action">

                            📁 ${project.nummer} - ${project.naam}

                        </a>
                    `;

                });

            }

            // Offertes
            if (data.offertes.length > 0) {

                html += `
                    <div class="list-group-item active">
                        <i class="bi bi-file-earmark-text"></i>
                        Offertes
                    </div>
                `;

                data.offertes.forEach(offerte => {

                    html += `
                        <a href="/offerte/${offerte.id}"
                           class="list-group-item list-group-item-action">

                            📄 ${offerte.nummer}

                        </a>
                    `;

                });

            }

            // Materialen
            if (data.materialen.length > 0) {

                html += `
                    <div class="list-group-item active">
                        <i class="bi bi-box-seam"></i>
                        Materialen
                    </div>
                `;

                data.materialen.forEach(materiaal => {

                    html += `
                        <a href="/materiaal/${materiaal.id}"
                           class="list-group-item list-group-item-action">

                            📦 ${materiaal.omschrijving}

                        </a>
                    `;

                });

            }

            if (html === "") {

                html = `
                    <div class="list-group-item text-muted">

                        Geen resultaten gevonden.

                    </div>
                `;

            }

            resultsBox.querySelector(".list-group").innerHTML = html;
            resultsBox.style.display = "block";

        }

        catch (err) {

            console.error(err);

        }

    });

    // Zoekresultaten sluiten bij klik buiten de zoekbalk
    document.addEventListener("click", function(e){

        if(
            !resultsBox.contains(e.target) &&
            e.target !== searchInput
        ){

            resultsBox.style.display = "none";

        }

    });

    // Resultaten weer tonen bij focus
    searchInput.addEventListener("focus", function(){

        if(
            resultsBox.querySelector(".list-group").innerHTML !== ""
        ){

            resultsBox.style.display = "block";

        }

    });

}