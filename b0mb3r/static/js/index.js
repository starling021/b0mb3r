const input = document.querySelector('#phone');
let intlTelInput;
let bar;

const countryPlaceholderMap = {
    ru: "912 345-67-89",
    ua: "50 123 4567",
    kz: "771 000 9998",
    by: "29 491-19-11",
    custom: "1 202-555-0135"
};

document.addEventListener('DOMContentLoaded', () => {
    window.intlTelInputGlobals.getCountryData().push({
        name: "Нет в списке",
        iso2: "custom",
        dialCode: "",
        priority: 0,
        areaCodes: null
    });
    intlTelInput = window.intlTelInput(input, {
        onlyCountries: ['ru', 'ua', 'kz', 'by', 'custom'],
        initialCountry: 'ru',
        separateDialCode: true,
    });

    bar = new ProgressBar.Circle(document.querySelector("#loader"), {
        strokeWidth: 12,
        color: '#dc3545',
        trailColor: '#eee',
        trailWidth: 12,
        svgStyle: null
    });
});

input.addEventListener("countrychange", () => {
    input.placeholder = countryPlaceholderMap[intlTelInput.getSelectedCountryData().iso2];
});

document.querySelector("#main-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    setTimeout(() => document.querySelector('#block-ui').style.display = "block", 850);
    document.querySelector('main').style.cssText = "animation:blur; animation-duration:850ms; animation-fill-mode:both";
    document.querySelector('footer').style.cssText = document.querySelector('main').style.cssText;
    document.querySelector('#loader').style.cssText = "animation:fadeIn; animation-duration:850ms; animation-fill-mode:both";

    const formData = new FormData(document.querySelector('#main-form'));
    formData.append('phone_code', intlTelInput.getSelectedCountryData().dialCode);
    await fetch("/attack/start", {
        method: 'POST',
        body: formData,
    });

    const interval = setInterval(async () => {
        await fetch("/attack/status", {
            method: 'GET'
        }).then((response) => {
            return response.json();
        }).then((data) => {
            bar.animate(100 / data.end_at * data.currently_at / 100, {duration: 250});

            if (data.end_at === data.currently_at) {
                clearInterval(interval);
                setTimeout(() => document.querySelector('#block-ui').style.display = "none", 850);
                document.querySelector('#loader').style.cssText = "animation:fadeOut; animation-duration:850ms; animation-fill-mode:both";
                document.querySelector('main').style.cssText = "animation:blur; animation-duration:850ms; animation-fill-mode:both; animation-direction:reverse";
                document.querySelector('footer').style.cssText = document.querySelector('main').style.cssText;
            }
        });
    }, 500);
});
