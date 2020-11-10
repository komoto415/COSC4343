const CLEARANCE_MAP = {
    'T': {
        'name': 'TOP-SECRET',
        'access': 4
    },
    'S': {
        'name': 'SECRET',
        'access': 3
    },
    'C': {
        'name': 'CONFIDENTIAL',
        'access': 2
    },
    'U': {
        'name': 'UNCLASSIFED',
        'access': 1
    }
}

const IMAGE_NAMES = ['Unclassified', 'Confidential', 'Secret', 'TopSecret']

function render() {
    let username = localStorage.getItem('username');
    let clearance = localStorage.getItem('clearance');
    let clearanceName = CLEARANCE_MAP[clearance]['name']
    let clearanceAccess = CLEARANCE_MAP[clearance]['access']
    document.getElementById('welcome').innerHTML = `Welcome back ${username}!`;
    document.getElementById('flavour').innerHTML = `It looks like your clearnace level is ${clearanceName}. 
    This means you have access to ${clearanceAccess} image${clearanceAccess > 1  ? 's' : ''}.`;
    let wrapper = document.getElementById('clearance-wrapper');
    for (var i = 0; i < clearanceAccess; i++) {
        console.log(IMAGE_NAMES[i])
        let br = document.createElement('BR');
        wrapper.appendChild(br);

        let imgDiv = document.createElement('IMG');
        imgDiv.setAttribute('src', `./imgs/${IMAGE_NAMES[i]}.png`);
        imgDiv.setAttribute('height', '200')
        wrapper.appendChild(imgDiv);
    }
}