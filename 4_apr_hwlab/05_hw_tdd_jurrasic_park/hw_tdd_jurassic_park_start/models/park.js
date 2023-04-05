const Park = function (name, ticketPrice) {
    this.name = name
    this.ticketPrice = ticketPrice
    this.dinosaurs = []
}

Park.prototype.noOfDinosaurs = function () {
    return this.dinosaurs.length
}

Park.prototype.addDinosaur = function (dinosaur) {
    this.dinosaurs.push(dinosaur)
}

Park.prototype.removeDinosaur = function(dinosaur){
    const indexPos = this.dinosaurs.indexOf(dinosaur)
    this.dinosaurs.splice(indexPos,1)
}

Park.prototype.popularDino = function () {
    let MostPopDino = this.dinosaurs[0]
    
    for (const dinosaur of this.dinosaurs) {
        if (dinosaur.guestsAttractedPerDay > MostPopDino.guestsAttractedPerDay)
        MostPopDino = dinosaur

    }
    return MostPopDino
}

Park.prototype.dinoBySpecies = function (species) {
    const speciesList = []
    for (const dinosaur of this.dinosaurs) {
        if (dinosaur.species === species) {
            speciesList.push(dinosaur)
        }
    }
    return speciesList
}

Park.prototype.headCount = function(){
    let count = 0

    for (const dinosaur of this.dinosaurs) {
        count += dinosaur.guestsAttractedPerDay
    }

    return count
}

Park.prototype.headCountPerYear = function(){
    return this.headCount() * 365
    // let count = 0

    // for (const dinosaur of this.dinosaurs) {
    //     count += (dinosaur.guestsAttractedPerDay * 365)
    // }

    // return count
}

Park.prototype.yearlyTotal = function () {
    return (this.headCountPerYear() * this.ticketPrice)
}

// Park.prototype.removeBySpecies = function (species) {
//     for (const dinosaur of this.dinosaurs) {
//         if (dinosaur.species === species) {
//             const indexPos = this.dinosaurs.indexOf(dinosaur)
//             this.dinosaurs.splice(indexPos, 1)
// }}}

Park.prototype.removeBySpecies = function (species) {
    const speciesList = []
    for (const dinosaur of this.dinosaurs) {
        if (dinosaur.species !== species) {
            speciesList.push(dinosaur)
        }
    }
    this.dinosaurs = speciesList
}

Park.prototype.numberByDietType = function () {
    const diet = {carnivore: 0;
    }
    diet[this.dinosaurs.diet]
}

module.exports = Park