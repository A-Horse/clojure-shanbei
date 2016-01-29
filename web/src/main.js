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
        url: apiAddress('add'),
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

let queryWord = () => {
    
};

let learnThisWord = (word, status) => {
    
};


// addWord('appleeee');

console.log('Happly every day!');
