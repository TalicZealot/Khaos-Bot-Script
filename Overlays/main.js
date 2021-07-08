let khaosSlideshow = $("#khaos-slideshow");

let commandStartingCooldowns = {};
for (const [key, value] of Object.entries(commands)) {
    if (value.startsOnCooldown) {
        commandStartingCooldowns[key] = value.cooldown;
    }
    value.cooldown = 0;
}

//generate html elements for every command in order
function createCommandElements() {

    let commandCounter = 0;
    let newContainer = $('<div class="khaos-container"></div>');
    let newCommands = $('<div class="khaos-commands"><div class="command-header smaller-font">command</div></div>');
    let newPrices = $('<div class="khaos-prices"><div class="command-header smaller-font">cost</div></div>');
    let newCooldowns = $('<div class="khaos-cooldowns"><div class="command-header smaller-font">cooldown</div></div>');

    let orderedCommands = [];
    for (const [key, value] of Object.entries(commands)) {
        orderedCommands[value.index] = value;
    }

    for (let i = 0; i < orderedCommands.length; i++) {
        let command = orderedCommands[i];
        if (commandCounter > 6) {
            commandCounter = 0;
            newContainer.append(newCommands);
            newContainer.append(newPrices);
            newContainer.append(newCooldowns);
            khaosSlideshow.append(newContainer);

            newContainer = $('<div class="khaos-container"></div>');

            newCommands = $('<div class="khaos-commands"><div class="command-header smaller-font">command</div></div>');
            newPrices = $('<div class="khaos-prices"><div class="command-header smaller-font">cost</div></div>');
            newCooldowns = $('<div class="khaos-cooldowns"><div class="command-header smaller-font">cooldown</div></div>');
        }

        let newCommand = $(`<div id="${command.command}-command" class="command"></div>`);
        newCommand.html("!" + command.command);
        if (command.command.length > 11) {
            newCommand.addClass('smaller-font');
        }
        newCommands.append(newCommand);

        let newPrice = $(`<div id="${command.command}-cost" ></div>`);
        newPrice.html(command.cost);
        newPrices.append(newPrice);

        let newCooldown = $(`<div class="command-cooldown"><span id="${command.command}-cooldown"></span></div>`);

        let newIcon = $(`<img id="${command.command}-icon" class="command-icon" src="IconEye.png" width="16" height="16"></img>`);

        switch (command.type) {
            case 1:
                newIcon = $(`<img id="${command.command}-icon" class="command-icon" src="IconSkull.png" width="16" height="16"></img>`);
                break;
            case 2:
                newIcon = $(`<img id="${command.command}-icon" class="command-icon" src="IconFairy.png" width="16" height="16"></img>`);
                break;
            default:
                break;
        }

        //newCooldown.html(command.cooldown);
        newCooldown.append(newIcon);
        newCooldowns.append(newCooldown);
        commandCounter++;
    }

    while (commandCounter < 7) {
        let newCommand = $('<div class="command"><br></div>');
        newCommands.append(newCommand);
        let newPrice = $('<div></div>');
        newPrices.append(newPrice);
        let newCooldown = $('<div class="command-cooldown"></div>');
        newCooldowns.append(newCooldown);
        commandCounter++;
    }

    newContainer.append(newCommands);
    newContainer.append(newPrices);
    newContainer.append(newCooldowns);
    khaosSlideshow.append(newContainer);

    $("#khaos-slideshow > div:gt(0)").hide();
}

function animationFrame() {
    $('#khaos-slideshow > div:first')
        .hide()
        .next()
        .fadeIn(500)
        .end()
        .appendTo('#khaos-slideshow');
}

function startAnimation() {
    setInterval(function() {
        animationFrame();
    }, 10000);
}

function timersTick() {
    setInterval(function() {
        for (const [key, value] of Object.entries(commands)) {
            if (value.cooldown > 0) {
                value.cooldown--;
                displayCooldown(value.command);
                if (value.cooldown == 0) {
                    $(`#${value.command}-command`).removeClass('onCooldown');
                    $(`#${value.command}-cost`).removeClass('onCooldown');
                    $(`#${value.command}-cooldown`).addClass('hidden');
                    $(`#${value.command}-icon`).removeClass('hidden');
                }
            }
        }
    }, 1000);
}

function displayCooldown(command) {
    let minutes = Math.floor(commands[command].cooldown / 60);
    let seconds = commands[command].cooldown - (minutes * 60);
    $(`#${command}-cooldown`).html(`${(minutes).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})}:${(seconds).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})}`);
}

function updateCommand(command, cost, cooldown) {
    $(`#${command}-cost`).html(cost);
    if (cooldown > 0) {
        $(`#${command}-command`).addClass('onCooldown');
        $(`#${command}-cost`).addClass('onCooldown');
        $(`#${command}-cooldown`).removeClass('hidden');
        $(`#${command}-icon`).addClass('hidden');
        commands[command].cooldown = cooldown * 60;
        displayCooldown(command);
    }
}

function activateStartingCooldown() {
    for (const [key, value] of Object.entries(commands)) {
        if (value.startsOnCooldown) {
            updateCommand(value.command, value.cost, commandStartingCooldowns[key]);
        }
    }
}

// Streamlabs Chatbot webosocket connection handling
function connectWebsocket() {
    var socket = new WebSocket(API_Socket);

    socket.onopen = function() {
        // Create authentication payload and request required events
        var auth = {
            author: "TalicZealot",
            website: "https://taliczealot.github.io/",
            api_key: API_Key,
            events: [
                "EVENT_UPDATE_COMMAND",
                "EVENT_START"
            ]
        };
        socket.send(JSON.stringify(auth));
    };

    // Ws OnClose : try reconnect
    socket.onclose = function() {
        socket = null;
        setTimeout(connectWebsocket, 5000);
    };

    // WS OnMessage event : handle events
    socket.onmessage = function(message) {
        // Parse message data to extract event name
        var socketMessage = JSON.parse(message.data);
        console.log(socketMessage);

        if (socketMessage.event == "EVENT_UPDATE_COMMAND") {
            var eventData = JSON.parse(socketMessage.data);
            updateCommand(eventData.command, eventData.cost, eventData.cooldown);
        } else if (socketMessage.event == "EVENT_START") {
            activateStartingCooldown();
        }
    };
}

// Initiate on document load
$(function() {
    // Show an error message if the API key file is not loaded
    if (typeof API_Key === "undefined") {
        $("#khaos-slideshow").html("<div>API Key file missing!<br>Right-click on the script in Streamlabs and select \"Insert API Key\"</div>");
    }
    // Connect to the Streamlabs Chatbot websocket
    else {
        connectWebsocket();
        createCommandElements();
        startAnimation();
        timersTick();
    }
});