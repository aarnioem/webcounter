*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Set counter to a value
    Go To  ${HOME_URL}
    Click Button  Nollaa
    Page Should Contain  nappia painettu 0 kertaa

    Input Text  value  10
    Click Button  Aseta
    Page Should Contain  nappia painettu 10 kertaa

Set counter to a negative value
    Go To  ${HOME_URL}
    Click Button  Nollaa
    Page Should Contain  nappia painettu 0 kertaa

    Input Text  value  -10
    Click Button  Aseta
    Page Should Contain  Invalid value