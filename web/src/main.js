'use strict';


import * as $ from 'jquery'; 

const setting  = {
    serverAddress: 'http://localhost:7777'
};

let apiAddress = (path) => {
    return setting.serverAddress.concat('/', path);
};

let addWord = (word, cb) => {
    $.ajax({
        url: apiAddress('word'),
        method: 'POST',
        data: {
            word: word
        },
        success: (data) => {
            console.log(data);
        },
        error: (xhr) => {
            
        }
    });
};

let getToLearnWord = () => {
    $.ajax({
        url: apiAddress('word'),
        method: 'GET',
        dataType: 'json',
        success: (data) => {
            console.log(data);
        },
        error: (xhr) => {
            
        }
    });
};

//getToLearnWord();


addWord('raspberry');

console.log('Happly every day!');
