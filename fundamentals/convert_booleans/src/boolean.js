module.exports = function isYesOrNey(bool) {
  if (bool === true) {
    bool = 'Yes';
  }
  if (bool === false) {
    bool = 'No';
  }

  return bool;
};
