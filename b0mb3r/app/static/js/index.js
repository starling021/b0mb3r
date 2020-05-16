const phoneInput = document.querySelector("#phone");
const serviceCount = document.querySelector("#serviceCount");
let intlTelInput, progressBar;

const countryPlaceholders = {
    ru: "912 345-67-89",
    ua: "50 123 4567",
    kz: "771 000 9998",
    by: "29 491-19-11",
    custom: "1 202-555-0135"
};

document.addEventListener("DOMContentLoaded", () => {
    window.intlTelInputGlobals.getCountryData().push({
        name: "Нет в списке",
        iso2: "custom",
        dialCode: "",
        priority: 0,
        areaCodes: null
    });
    intlTelInput = window.intlTelInput(phoneInput, {
        onlyCountries: ["ru", "ua", "kz", "by", "custom"],
        initialCountry: "ru",
        separateDialCode: true,
    });

    progressBar = new ProgressBar.Circle(document.querySelector("#loader"), {
        strokeWidth: 12,
        color: "#dc3545",
        trailColor: "#eee",
        trailWidth: 12,
        svgStyle: null
    });
});

phoneInput.addEventListener("countrychange", async () => {
    let countResponse = await fetch("/services/count?country_code=" + intlTelInput.getSelectedCountryData().dialCode, {
        method: "GET",
    });
    let content = await countResponse.json();
    serviceCount.innerHTML = content.count;

    phoneInput.placeholder = countryPlaceholders[intlTelInput.getSelectedCountryData().iso2];
});

document.querySelector("#main-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    setTimeout(() => document.querySelector("#block-ui").style.display = "block", 850);
    blurDocument();
    document.querySelector("#loader").style.cssText =
        "animation:fadeIn; " +
        "animation-duration:850ms; " +
        "animation-fill-mode:both";

    let phone = intlTelInput.getSelectedCountryData().dialCode + document.querySelector("#phone").value;

    let response = await fetch("/attack/start", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            number_of_cycles: document.querySelector("#count").value,
            phone: phone
        }),
    });

    let attackResponse = await response.json();

    const interval = setInterval(async () => {
        let response = await fetch("/attack/" + attackResponse.id + "/status", {
            method: "GET"
        });
        let statusResponse = await response.json();
        progressBar.animate(100 / statusResponse.end_at * statusResponse.currently_at / 100, {
            duration: 250
        });

        if (statusResponse.end_at === statusResponse.currently_at) {
            clearInterval(interval);
            setTimeout(() => document.querySelector("#block-ui").style.display = "none", 850);
            unblurDocument();
            document.querySelector("#loader").style.cssText =
                "animation:fadeOut; " +
                "animation-duration:850ms; " +
                "animation-fill-mode:both";
        }
    }, 500);
});

function blurDocument() {
    let cssText =
        "animation:blur; " +
        "animation-duration:850ms; " +
        "animation-fill-mode:both";
    document.querySelector("main").style.cssText = document.querySelector("footer").style.cssText = cssText;
}

function unblurDocument() {
    let cssText = "animation:blur; " +
        "animation-duration:850ms; " +
        "animation-fill-mode:both; " +
        "animation-direction:reverse";
    document.querySelector("main").style.cssText = document.querySelector("footer").style.cssText = cssText;
}