const AuthenticationUser = artifacts.require("AuthenticationUser");

module.exports = function (deployer) {
  deployer.deploy(AuthenticationUser);
};
