*** Settings ***
Library           ExtendedSelenium2Library
Library           Collections
Variables         ..\\PageObjects\\Locators.py
Library           RequestsLibrary
Library           requests
Library           HttpLibrary.HTTP
Library           String
Library           DateTime
Library           ImageHorizonLibrary

*** Keywords ***
Read Variables from Excel
    Open Excel    ${Excel_File_Path}${Filename}
    ${base_invurl}=    Read Cell Data By Name    ${SheetName}    B1
    ${URL}=    Read Cell Data By Name    ${SheetName}    B2
    ${username} =    Read Cell Data By Name    ${SheetName}    B3
    ${password} =    Read Cell Data By Name    ${SheetName}    B4
    ${offername}=    Read Cell Data By Name    ${SheetName}    B5
    ${custname} =    Read Cell Data By Name    ${SheetName}    B6
    ${lastname} =    Read Cell Data By Name    ${SheetName}    B7
    ${subcategory}=    Read Cell Data By Name    ${SheetName}    B8
    ${nationid} =    Read Cell Data By Name    ${SheetName}    B9
    ${location} =    Read Cell Data By Name    ${SheetName}    B10
    ${postaddress}=    Read Cell Data By Name    ${SheetName}    B11
    ${city}=    Read Cell Data By Name    ${SheetName}    B12
    ${landmark} =    Read Cell Data By Name    ${SheetName}    B13
    ${filelocation}=    Read Cell Data By Name    ${SheetName}    B14
    ${dateofbirth}=    Read Cell Data By Name    ${SheetName}    B15
    Set Suite Variable    ${base_invurl}
    Set Suite Variable    ${URL}
    Set Suite Variable    ${username}
    Set Suite Variable    ${password}
    Set Suite Variable    ${offername}
    Set Suite Variable    ${custname}
    Set Suite Variable    ${lastname}
    Set Suite Variable    ${subcategory}
    Set Suite Variable    ${nationid}
    Set Suite Variable    ${location}
    Set Suite Variable    ${postaddress}
    Set Suite Variable    ${city}
    Set Suite Variable    ${landmark}
    Set Suite Variable    ${filelocation}
    Set Suite Variable    ${dateofbirth}

Get SIM ICCID
    @{res}=    requests.get    ${base_invurl}
    Log Many    ${res}
    ${SIM}=    Convert to String    ${res}
    ${SIMICCID}=    get substring    ${SIM}    56    72
    Set Suite Variable    ${SIMICCID}

Login to DCLM
    ${values}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${values}    add_argument    --incognito
    Create Webdriver    Chrome    chrome_options=${values}
    Go To    ${URL}
    Maximize Browser Window
    click element    ${btn_advcsecrty}
    wait until element is enabled    ${ele_chooseadvcsecrty}
    click element    ${ele_chooseadvcsecrty}
    Input text    ${txt_username}    ${username}
    Input text    ${txt_password}    ${password}
    click button    ${ele_loginsubmit}
    sleep    6
    title should be    DCLM 5.0.0

Search my Offer
    click button    ${btn_offmenu}
    input text    ${ele_offersrch}    ${offername}
    sleep    2
    click button    ${btn_srchbtnoff}
    sleep    5
    element text should be    ${ele_planname}    ${offername}
    wait until element is enabled    ${btn_addtocart}    15
    click button    ${btn_addtocart}
    sleep    2

Enter my Customer Details
    ${EMAIL}=    Generate Random String    4    [NUMBERS]
    input text    ${ele_email}    ttautomate.${EMAIL}@gmail.com
    Set Suite Variable    ${EMAIL}
    sleep    2
    input text    ${ele_custname}    ${custname}
    input text    ${ele_lastname}    ${lastname}
    wait until element is enabled    ${btn_proceedfrmcust}
    click button    ${btn_proceedfrmcust}
    wait until element is enabled    ${btn_proceedfrmlead}    10
    click button    ${btn_proceedfrmlead}
    sleep    5

Inventory SIM input
    input text    ${ele_siminp}    ${SIMICCID}
    sleep    2
    click element    ${ele_mouseout}
    sleep    2
    click button    ${btn_invproceed}
    sleep    5

Enter Customer Info
    click element    ${ele_subcategory}
    click element    ${ele_subcatlist}
    sleep    2
    input text    ${ele_idnum}    ${nationid}
    sleep    2
    click element    ${ele_dateofbirth}
    input text    ${ele_dob}    ${dateofbirth}
    sleep    2
    click element    ${ele_mouseout1}

Enter Address
    scroll element into view    ${ele_addressheading}
    input text    ${ele_address}    ${postaddress}
    sleep    2
    scroll element into view    ${ele_address}
    wait until element is visible    ${ele_city}
    input text    ${ele_city}    ${city}
    Press Key    ${ele_city}    \\13
    sleep    2
    ${postcode}=    Generate Random String    4    [NUMBERS]
    input text    ${ele_postalcode}    ${postcode}
    input text    ${ele_landmark}    ${landmark}
    sleep    2
    scroll element into view    ${ele_sameasresaddr}
    wait until element is enabled    ${ele_sameasresaddr}
    Select Checkbox    ${ele_sameasresaddr}
    Checkbox Should Be Selected    ${ele_sameasresaddr}
    wait until element is enabled    ${ele_sameasbilladdr}
    Select Checkbox    ${ele_sameasbilladdr}
    Checkbox Should Be Selected    ${ele_sameasbilladdr}

Billing details selection
    scroll element into view    ${ele_billdetailheader}
    sleep    2
    click element    ${ele_periodicity}
    click element    ${ele_monthperiod}
    sleep    2
    click element    ${ele_billcycle}
    click element    ${ele_1stbillcycle}
    sleep    2

Choose document type
    scroll element into view    ${ele_scrolltodoc}
    sleep    2
    Click Element    ${ele_doctype}
    Click Element    ${ele_doctypelist}
    Input text    ${ele_doclocation}    ${location}
    click element    ${ele_docdate}
    Press Combination    key.ctrl    key.a
    Press Combination    key.ctrl    key.c
    Press Combination    key.ctrl    key.v
    Press Combination    key.ctrl    key.v
    Press Combination    key.ctrl    key.z
    Click Element    ${ele_mouseout2}
    Wait until element is enabled    ${ele_waitforchoosefile}
    sleep    3
    choose file    ${ele_choosefile}    ${filelocation}
    sleep    3

Choose document type in address proof
    click element    ${ele_doctypeaddrproof}
    click element    ${ele_doctypeaddrprooflist}

Choose document type in age proof
    scroll element into view    ${ele_scrlageproof}
    sleep    2
    click element    ${ele_doctypeageproof}
    click element    ${ele_doctypeageprooflist}
    click button    ${btn_proceedreg}
    sleep    2

Payment page
    wait until element is enabled    ${btn_addpayment}
    click button    ${btn_addpayment}
    sleep    3
    wait until element is enabled    ${btn_proceedpay}    10
    click button    ${btn_proceedpay}
    Capture Page Screenshot    RegFinal.png
    sleep    2

Go to dashboard
    wait until element is enabled    ${btn_gotodashboard}    10
    sleep    3
    click button    ${btn_gotodashboard}
    sleep    6
    wait until element is enabled    ${ele_custidpopup}    10
    ${custid}=    Get Text    ${ele_custidpopup}
    Set Global Variable    ${custid}

Check Request & 360
    click element    ${btn_requestpage}
    click element    ${txt_srchcust}
    input text    ${txt_srchcust}    ${custid}
    sleep    2
    wait until element is enabled    ${ele_inpcust}    10
    click element    ${ele_inpcust}
    sleep    10
    capture page screenshot    360degview.png
    sleep    2
