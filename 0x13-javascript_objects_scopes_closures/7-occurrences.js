#!/usr/bin/node
exports.nbOccurences = function (list, searchElement)  {
  let nOccurrences = list.filter(element => element === searchElement).length;
  return nOccurrences;
};
