*** Settings ***
Library           ExtendedSelenium2Library
Resource          ..//..//Resources//RegistrationKeywordR2.robot
Library           String
Library           Collections
Library           ExcelLibrary

*** Variables ***
${custid}         ${EMPTY}
${SIMICCID}       ${EMPTY}
${EMAIL}          ${EMPTY}
${postcode}       ${EMPTY}
${Excel_File_Path}    C:/Automation R2/Documents/
${Filename}       DCLM Details.xls
${SheetName}      RegDet

*** Test Cases ***
Read the variables
    [Tags]    Basic Input
    Read Variables from Excel
    Get SIM ICCID

Login DCLM
    [Tags]    Sanity Check of Login
    Login to DCLM

Search Offer
    [Tags]    Sanity
    Search my Offer

Enter Customer Details
    [Tags]    Input Customer details
    Enter my Customer Details

Inventory input
    [Tags]    Enter Inventory Details
    Inventory SIM input

Basic info
    [Tags]    Enter Customer Info
    Enter Customer Info
    Enter Address
    Billing details selection
    Choose document type
    Choose document type in address proof
    Choose document type in age proof

Proceed to payment page
    [Tags]    Payment
    Payment page
    Go to dashboard

Check Customer in 360
    [Tags]    Sanity Check of Customer
    Check Request & 360
