function nutricodeGetImg(product_nutriscore){
    console.log("test")
    var listLetter = ["a","b","c","d","e"];
    var listImg = []
        for (letter in listLetter) {
            if (letter == product_nutriscore) {
                var myImage = document.createElement('img');
                myImage.setAttribut('src', '../../img/nutricode/nutri_'+letter+'.png', 'alt', 'nutricode');
                listImg[letter] = myImage;

        var myDiv = document.getElementById(product_show);
        myDiv.appendChild(listImg[letter]);
             }
        }
}