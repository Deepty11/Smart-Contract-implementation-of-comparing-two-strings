// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 ;

contract AuthenticationUser{
    

    struct User{
        string name;
        string contact;
        string IMEI;
    }
    // mapping (uint=> User) public users;
    User[] public users;
   
    constructor() public{
        createUser("Rahim","12376546","32486873264");
        createUser("Karim","12376946","32478673264");
        createUser("Mahim","12396546","32489773264");

    }

    function createUser(string memory _name, string memory _contact, string memory _IMEI)public {
        // users[_id]=User(_name,_contact,_IMEI);
        User memory user=User(_name,_contact,_IMEI);
        users.push(user);
    }
    function getUserById(uint _id) public view returns (string memory _name, 
                                                        string memory  _contact,string memory  _IMEI){
        
        User memory user=users[_id];
        return(user.name,user.contact,user.IMEI);


    }
    function getUserNameById(uint _id) public view returns (string memory _name){
        
        User memory user=users[_id];
        return(user.name);


    }
    function getUserIMEIById(uint _id) public view returns (string memory  _IMEI){
        
        User memory user=users[_id];
        return(user.IMEI);


    }

    function compareIMEI(string memory fetched_IMEI) public view returns (string memory _name){

        bool res=false;
        for(uint i=0;i<3;i++){
            string memory  userIMEI= getUserIMEIById(i);
            if(bytes(userIMEI).length== bytes(fetched_IMEI).length){
                res=(keccak256(abi.encodePacked(userIMEI))==keccak256(abi.encodePacked(fetched_IMEI)));
                
            }
            if(res==true){
                return getUserNameById(i);
            }

        }
        return "UNKNOWN";

    }



}