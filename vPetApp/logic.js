let pet = {
    hunger: 50,
    happiness: 50
};

function updateBars() {
    document.getElementById('hungerBar').style.width = pet.hunger + '%';
    document.getElementById('happinessBar').style.width = pet.happiness + '%';
}

function feedPet() {
    if (pet.hunger > 0) {
        pet.hunger -= 10;
        pet.happiness += 5;
    }
    updateBars();
}

function playWithPet() {
    if (pet.happiness < 100) {
        pet.happiness += 10;
        pet.hunger += 5;
    }
    updateBars();
}

function yellAtPet() {
    if (pet.happiness < 100) {
        pet.happiness -= 10;
        pet.hunger -= 5;
    }
    updateBars();
}

setInterval(() => {
    pet.hunger += 5;
    pet.happiness -= 5;
    updateBars();
}, 5000);

updateBars();