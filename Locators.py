btn_srch =  "//*[@id='root']/div/div/div[2]/div/div/div[1]/header/div/div[1]/div[1]/button"
ele_customer = "//*[@id='root']/div/div/div[2]/div/div/div[1]/header/div/div[1]/div[2]"
ele_360servicepage = "//*[@id='root']/div/div/div[2]/div/section/section/div[3]/div[1]/div/ul/div/div/span/a/div"
btn_srchin360 = "//*[@id='root']/div/div/div[2]/div/section/section/div[1]/header/div/div[1]/div/button"
ele_custin360 = "//*[@id='root']/div/div/div[2]/div/section/section/div[1]/header/div/div[1]/div[2]"

#Service Request for Suspend
btn_service = "//*[@id='root']/div/div/div[2]/div/section/section/div[1]/header/div/div[3]/button[1]"
ele_suspend = "//*[@id='root']/div/div/div[2]/div/section/section/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul[3]"

#Perform Suspend
ele_checkboxsuspend = "//*[@id='suspension']/div/div[2]/div/div[1]/span/span[1]/input"
btn_gotodashboard = "//html/body/div[2]/div[2]/div/div[3]/div/button"

#Service Request for Resume
ele_resume = "//*[@id='root']/div/div/div[2]/div/section/section/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul[2]"

#Perform Resume
ele_resumecheckbox = "//*[@id='customerInfo']/div/div[2]/div[2]/div[1]/span/span[1]/input"

#Service Request for Terminate
ele_terminate = "//*[@id='root']/div/div/div[2]/div/section/section/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul[4]"

#Perform Terminate
ele_checkboxterminate ="//*[@id='termination']/div/div[2]/div[2]/div[1]/span/span[1]/input"

#Click on Request in 360
btn_request = "//*[@id='root']/div/div/div[2]/div/section/section/div[4]/div[2]/header/div/div/div/div/button[3]"

#click somewhere else

#--------------------------------------------------------------------------------------------------------------------#
#service request 162 env
#360 service page
ele_360service="//*[@id='root']/div/div/div[1]/section/div[2]/div/div[1]/div/ul/div/div[1]"
               

#services search
btn_srchservice="//*[@id='root']/div/header/div/div[1]/header/div/div[3]/button[1]"

#search suspension option
ele_suspopt="//*[@id='root']/div/header/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul/a[3]/div"
        

#proceed to suspend
btn_proceedservice="//*[@id='root']/div/div/div[1]/div[3]/div[2]/div/div/div[3]/div/button"

#click elsewr in service
ele_elsewrservice="//*[@id='root']/div/div/div[1]/section/div[2]/main/div[2]/div[1]/div/div/div[2]"

#request button in service page
btn_reqservice="//*[@id='root']/div/div/div[1]/section/div[2]/main/div[2]/div[2]/header/div/div/div/div/button[3]"

#search revoke option
ele_revopt="//*[@id='root']/div/header/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul/a[2]/div"
#search terminate option
ele_termopt="//*[@id='root']/div/header/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul/a[4]/div"

#add to payment in service req
btn_addpayservice="//*[@id='root']/div/div/div[1]/div[3]/div[1]/div[3]/div/div[2]/div/div/div/form/div[2]/button"

#proceed to complete in service
btn_proceedservice="//*[@id='root']/div/div/div[1]/div[3]/div[2]/div/div/div[3]/div/button"

#go to dashboard service
btn_gotodashboardservice="//html/body/div[2]/div[2]/div/div[3]/div/button"

#checkbox for revoke service
chkbx_revoke="//*[@id='customerInfo']/div/div[2]/div[2]/div[1]/span/span[1]/input"

#termination service
ele_termlink="//*[@id='root']/div/header/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul/a[4]/div"

#add vas link
ele_addvaslink="//*[@id='root']/div/header/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/ul/a[1]/div"

#vas bundle add to cart
btn_addtocartvasbund="//*[@id='root']/div/div/div[1]/div[4]/main/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div[4]/div[2]/button"

#vas proceed
btn_proceedvas="//*[@id='root']/div/div/div[1]/div[4]/main/div/div[2]/div/div/div[3]/div/button"

#vas proceed to complete
btn_proceedvascomp="//*[@id='root']/div/div/div[1]/div[4]/div/form/div/div[2]/div/div/div[3]/div/button"

#vas add to payment
btn_addtopayvas="//*[@id='root']/div/div/div[1]/div[4]/div[1]/div[3]/div/div[2]/div/div/div/form/div[2]/button"

#vas proceed from payment
btn_proceedpaymentvas="//*[@id='root']/div/div/div[1]/div[4]/div[2]/div/div/div[3]/div/button"

#choose VAS orders from 360
btn_vasrequest="//*[@id='root']/div/div/div[1]/section/div[2]/main/div[2]/div[2]/header/div/div/div/div/button[4]"

#terminate checkbox
ele_termchkbx="//*[@id='termination']/div/div[2]/div[3]/div[1]/span/span[1]/input"
#-----------------------------------------------------------------------------------------------------------------------------------------#
#Registration process
#select advanced security
btn_advcsecrty="//*[@id='details-button']"
ele_chooseadvcsecrty="//*[@id='proceed-link']"

# Login Page Elements
txt_username = "//*[@id='username']"
txt_password = "//*[@id='password']"
ele_loginsubmit="//*[@id='submit']"

#Search offer
ele_offersrch="//*[@id='root']/div/div/div[1]/div[1]/header/div/div[1]/div/div/input"
btn_offmenu= "//*[@id='root']/div/div/div[1]/div/div/div/div[2]/button[3]"
ele_planname= "//*[@id='root']/div/div/div[1]/div[3]/main/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/h5"
btn_srchbtnoff="//*[@id='root']/div/div/div[1]/div[1]/header/div/div[1]/div/button[1]"
btn_addtocart="//*[@id='root']/div/div/div[1]/div[3]/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div/div[4]/div/button"

#Enter Customer Details
ele_email= "//*[@id='email']"
ele_custname= "//html/body/div[5]/div[2]/div/div[2]/form/div/div[1]/div[2]/p/div/div/input"
ele_lastname="//html/body/div[5]/div[2]/div/div[2]/form/div/div[2]/div[2]/p/div/div/input"
btn_proceedfrmcust="//html/body/div[5]/div[2]/div/div[3]/div/button[2]"
btn_proceedfrmlead="//*[@id='root']/div/div/div[1]/div[3]/main/div/div[2]/div/div/div[3]/div/button"

#SIM Input
ele_siminp="//*[@id='root']/div/div/div[1]/div[4]/div/form/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/input"
ele_mouseout="//*[@id='root']/div/div/div[1]/div[3]"
btn_invproceed="//*[@id='root']/div/div/div[1]/div[4]/div/form/div/div[2]/div/div/div[3]/div/button"

#Basic info
ele_subcategory="//*[@id='select-customerSubCategory']"
ele_subcatlist="//*[@id='menu-customerSubCategory']/div[2]/ul/li[4]"
ele_idnum="//*[@id='customerInfo']/div/div[2]/div/div[6]/p/div/div/input"
ele_dateofbirth="//*[@id='customerInfo']/div/div[2]/div/div[8]/h5/div/div/div/div[1]"
ele_mouseout1="//*[@id='root']/div/div/div[1]/div[3]/div[5]"
ele_dob="//*[@id='date']"
#address info
ele_addressheading="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[1]"
ele_address="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/p[1]/div/div/input"
ele_postalcode="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[5]/p/div/div/input"
ele_landmark="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[6]/p/div/div/input"
ele_sameasresaddr="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[1]/label/span[1]/span[1]/input"
ele_sameasbilladdr="//*[@id='contactAddressInfo']/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[3]/div[2]/label/span[1]/span[1]/input"  
ele_city="//*[@id='react-select-3-input']"

#Billing Details
ele_billdetailheader="//*[@id='billingDetails']/div/div/h5"
ele_periodicity="//*[@id='select-periodicity']"
ele_monthperiod="//*[@id='menu-periodicity']/div[2]/ul/li"
ele_billcycle="//*[@id='select-billCycle']"
ele_1stbillcycle="//*[@id='menu-billCycle']/div[2]/ul/li[1]"

#Upload document
ele_scrolltodoc="//*[@id='documentDetails']/div/div/div[1]/div[1]/h5"
ele_doctype="//*[@id='select-uploadDocuments.POID.documentType']"
ele_doctypelist="//*[@id='menu-uploadDocuments.POID.documentType']/div[2]/ul/li[2]"
ele_docdate="//*[@id='documentDetails']/div/div/div[2]/div[1]/div/div[3]/p/div/div/div/div[1]"
ele_mouseout2="//*[@id='root']/div/div/div[1]/div[1]/header/div/div[1]"
ele_idnumdoc="//*[@id='documentDetails']/div/div/div[2]/div[1]/div/div[2]/p/div/div/input"
ele_doclocation="//*[@id='documentDetails']/div/div/div[2]/div[1]/div/div[4]/p/div/div/input"
ele_waitforchoosefile="//*[@id='documentDetails']/div/div/div[2]/div[2]/label/div/div/div/input"
ele_choosefile="//*[@id='documentDetails']/div/div/div[2]/div[2]/label/div/div/div/input"

#Address proof
ele_doctypeaddrproof="//*[@id='select-uploadDocuments.addressProof.documentType']"
ele_doctypeaddrprooflist="//*[@id='menu-uploadDocuments.addressProof.documentType']/div[2]/ul/li[2]"

#Age proof
ele_scrlageproof="//*[@id='documentDetails']/div/div/div[4]/div[1]/h5"
ele_doctypeageproof="//*[@id='select-uploadDocuments.ageProof.documentType']"
ele_doctypeageprooflist="//*[@id='menu-uploadDocuments.ageProof.documentType']/div[2]/ul/li[2]"

#Payment
btn_proceedreg="//*[@id='root']/div/div/div[1]/div[4]/div[2]/div/div/div[3]/div/button"
btn_addpayment="//*[@id='root']/div/div/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div/div/form/div[2]/button"
btn_proceedpay="//*[@id='root']/div/div/div[1]/div[4]/div[2]/div/div/div[3]/div/button"

#go to dashboard
btn_gotodashboard="//html/body/div[2]/div[2]/div/div[3]/div/button[2]"
ele_custidpopup="//*[@id='alert-dialog-description']/div[2]/div[3]"

#request page
btn_requestpage="//*[@id='root']/div/div/div[1]/div/div/div/div[2]/button[2]"
txt_srchcust = "//*[@id='inputBase']"
ele_inpcust="//*[@id='root']/div/header/div/div[1]/header/div/div[1]/div[2]/div"

