// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;

contract HelloWorld{

//   string public greetings;


//   function sayHello(string memory a) public{
//         greetings= a;
//     }
    string public main_IMEI="123456";
    string public payload;
    function setPayload(string memory content) public {
        payload = content;
    }
    function compareIMEI(string memory fetched_IMEI) public view returns (bool){
        if(bytes(main_IMEI).length!=bytes(fetched_IMEI).length){
            return false;
        }else{
            return (keccak256(abi.encodePacked(main_IMEI))==keccak256(abi.encodePacked(fetched_IMEI)));
        }

    }
}