const PangramFinder = function (phrase) {
  this.phrase = phrase
  this.alphabet = 'qwertyuiopasdfghjklzxcvbnm'.split('');
}

PangramFinder.prototype.isPangram = function () {
  return this.phrase.every(this.phrase === this.alphabet) 
}

module.exports = PangramFinder;
