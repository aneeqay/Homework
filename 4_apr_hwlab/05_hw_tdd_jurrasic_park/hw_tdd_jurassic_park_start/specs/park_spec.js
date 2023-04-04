const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function() {
  
  let park
  let stegosaurus
  let allosaurus

  beforeEach(function () {
    park = new Park("Jurassic Park", 100)
    stegosaurus = new Dinosaur("pink", "herbivore", 10)
    allosaurus = new Dinosaur("blue", "carnivore", 12)

  })

  it('should have a name', function () {
    assert.strictEqual(park.name, "Jurassic Park")
  });

  it('should have a ticket price', function () {
    assert.strictEqual(park.ticketPrice, 100)});

  it('should have a collection of dinosaurs', function () {
    actual = park.noOfDinosaurs()
    assert.strictEqual(actual, 0)
  });

  it('should be able to add a dinosaur to its collection', function () {
    park.addDinosaur(stegosaurus)
    actual = park.dinosaurs
    assert.deepStrictEqual(actual, [stegosaurus])
  });

  it('should be able to remove a dinosaur from its collection', function(){
    park.addDinosaur(stegosaurus)
    park.removeDinosaur(stegosaurus)
    actual = park.noOfDinosaurs()
    assert.strictEqual(actual, 0)
  });

  it('should be able to find the dinosaur that attracts the most visitors', function(){
    park.addDinosaur(stegosaurus)
    park.addDinosaur(allosaurus)
    actual = park.popDino()
    assert.strictEqual(actual, allosaurus)
  });

  it('should be able to find all dinosaurs of a particular species', function () {
    park.addDinosaur(stegosaurus)
    park.addDinosaur(allosaurus)
    actual = park.dinoBySpecies("blue")
    assert.deepStrictEqual(actual, [allosaurus])
  });

  it('should be able to calculate the total number of visitors per day', function(){
    park.addDinosaur(stegosaurus)
    park.addDinosaur(allosaurus)
    actual = park.headCount()
    assert.strictEqual(actual, 22)
  });


  it('should be able to calculate the total number of visitors per year', function(){
    park.addDinosaur(stegosaurus)
    park.addDinosaur(allosaurus)
    actual = park.headCountPerYear()
    assert.strictEqual(actual, (22*365))
  });

  it('should be able to calculate total revenue for one year', function () {
    park.addDinosaur(stegosaurus)
    park.addDinosaur(allosaurus)
    actual = park.yearlyTotal()
    assert.strictEqual(actual, (22*365*park.ticketPrice))
  });

});
