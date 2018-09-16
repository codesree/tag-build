from django.shortcuts import render
import json,time
from .mprocess import Monprocess
from .nprocess import Policy_starter
import requests
from .offline_composer import Composer

import os
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from .tests import asset_homecontent,asset_vehicle,asset_allrisks,report_builder,log_builder
from .test_gate import All_safe,gateway_process
from .test_chamber.testunit import awscert

from HtmlTestRunner import HTMLTestRunner,result
import unittest

from django.urls import resolvers,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import Userform
from .asset_manager import asset_manager

def index(request):
    context_dict = {'text': 'TAG - DASHBOARD'}
    return render(request, 'tag_home.html', context_dict)

def test_chamber(request):
    return render(request,'test_chamber_home.html')


def test_suite_home(request):

    return render(request,'asset_test_suite.html')

def asset_homecon_suite(request):

    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_homecontent))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')
    return render(request, 'asset_test_suite.html', {
        'tstat': 'hcdone',
        'logfile': logfil,
        'testrep': treprt
    })


def asset_vehicle_suite(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_vehicle))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')

    return render(request, 'asset_test_suite.html', {
        'tstat': 'mvdone',
        'logfile': logfil,
        'testrep': treprt
    })

def asset_allrisk_suite(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_allrisks))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')
    print('test report:',treprt)
    return render(request, 'asset_test_suite.html', {
        'tstat': 'ardone',
        'logfile': logfil,
        'testrep': treprt
    })


def startp(request):
    return render(request,"test_loader.html")


def test_load(request):
    time.sleep(5)

    print('hello')

    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    print(fname)
    print(lname)

    time.sleep(5)


    return render(request,"test_loader.html")


def test_report(request):

    print(treprt)
    tname = treprt['test_suite']
    tcase = treprt['test_cases']
    ttake = treprt['time_taken']
    tstrt = treprt['start_time']
    tendt = treprt['end_time']

    texe = 0
    tpas = 0
    tfal = 0

    for td in tcase:
        texe = texe + 1
        if td['status'] == 'PASS':
            tpas = tpas + 1
        elif td['status'] == 'FAIL':
            tfal = tfal + 1

    if tname == "asset_homecontent":
        tname = 'ASSET API FOR HOMECONTENTS RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "asset_allrisks":
        tname = 'ASSET API FOR ALL RISKS RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "asset_vehicle":
        tname = 'ASSET API FOR MOTOR VEHICLES RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '

    return render(request,'test_report.html',{
                                                'suitename':tname,
                                                'reporttitle':rname,
                                                'testcases':tcase,
                                                'timetaken':ttake,
                                                'starttime':tstrt,
                                                'endtime':tendt,
                                                'totaltests':texe,
                                                'totalpass':tpas,
                                                'totalfail':tfal
                                                })



def download_log(request):


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/test_chamber")
    log_file = os.path.join(LOG_DIR,logfil)
    print(log_file)

    if os.path.exists(log_file):
        print('log file found!!')

        with open(log_file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/json")
            #response['Content-Disposition'] = 'attachment; filename="logfile.json"'
            response['Content-Disposition'] = 'attachment; filename='+logfil+''
            return response


def download_assetrr(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/test_chamber")

    log_file = os.path.join(LOG_DIR,asset_rrl)
    print(log_file)

    if os.path.exists(log_file):
        print('log file found!!')

        with open(log_file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/json")
            #response['Content-Disposition'] = 'attachment; filename="logfile.json"'
            response['Content-Disposition'] = 'attachment; filename='+asset_rrl+''
            return response


@login_required
def beanstalk_home(request):
    return render(request, 'beanstalk_home.html')

@login_required
def beanstalk_quote(request):
    #reqf_obj = Reqform()
    #respf_obj = Respform()
    global startmon
    global createdq
    incom_post = 0
    incom_post_crq = False
    incom_post_acq = False
    incom_post_ctq = False

    if request.method == 'POST':
        crpost = request.POST.get('crpost')
        acpost = request.POST.get('acpost')
        ctpost = request.POST.get('ctpost')

        print(crpost)

        if crpost is not None:
            #check offline mode
            """api_req = request.POST.get('content')
            offline_pro(api_req,request)
            context_dict = {'text': 'API Gateway testing channel - TAG'}
            return render(request, 'tag_home.html', context_dict)"""

            # offline ends
            incom_post = crpost
            print("Posted...",incom_post)
        elif acpost is not None:
            incom_post = acpost
        elif ctpost is not None:
            incom_post = ctpost
        else:
            pass

        print("AM IN")
        api_req = request.POST.get('content')
        print(api_req)

        if incom_post == 'PROCEED WITH ACCEPT QUOTE':
            Resp_data = con_gatepro(api_req, request, 'ac_quote')
            incom_post_acq = True
        elif incom_post == 'PROCEED WITH CREATE QUOTE':
            createdq = api_req
            Resp_data = con_gatepro(api_req, request, 'cr_quote')
            incom_post_crq = True
        elif incom_post == 'PROCEED WITH POLICY CONVERSION':
            Resp_data = con_gatepro(api_req, request, 'conv_to_pol')
            incom_post_ctq = True
        else:
            context_dict = {'text': 'API Gateway testing channel - TAG'}
            return render(request, 'tag_home.html', context_dict)
        rdata = json.loads(Resp_data)
        print(type(rdata))
        req_bankd = json.loads(api_req)
        #chk_stat = rdata['bSuccess']
        #print("data:",chk_stat,"type of data:",type(chk_stat))
        #Decline part needs to be configured
        #
        # 1. PREPARE THE ACCEPT QUOTE JSON AND RELATE THEM
        # 2. SEND TO TAG
        #
        if rdata['bSuccess'] is True:
            if incom_post_crq is True:
                global dispq
                dispq = rdata['QuoteNumber']
                get_bankd = startmon.acq_bankupd(req_bankd)
                startmon = Monprocess('acq')
                acq_dat = startmon.acq_procdata(get_bankd, dispq)
                print("...............INSIDE CREATE PROCESS AND ACCEPT RETURN............................")
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': acq_dat,
                    'pantit': 'acq',
                    'dispq': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Success'
                })
            if incom_post_acq is True:
                dispq = dispq
                startmon = Monprocess('ctp')
                ctp_dat = startmon.ctp_procdata(dispq)
                print("...............INSIDE ACCEPT PROCESS AND CONVERT RETURN............................")
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': ctp_dat,
                    'pantit': 'ctp',
                    'dispq': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Success'
                })
            if incom_post_ctq is True:
                dispq = req_bankd['QuoteNumber']
                # startmon = Monprocess('ctp')
                # ctp_dat = startmon.ctp_procdata(dispq)
                log_policy(createdq,dispq, "tester")
                print("...............INSIDE CONVERT PROCESS PROCESS AND DONE............................")
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': 'PROCESS COMPLETED',
                    'pantit': 'ctp',
                    'dispp': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Success'
                })
        elif rdata['bSuccess'] is False:
            if incom_post_crq is True:
                dispq = False
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': 'Unable process the Accept quote due to an error.... See below',
                    'pantit': 'crq',
                    'dispq': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Failed',
                    'restart':'yes'
                })
            if incom_post_acq is True:
                dispq = False
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': 'Unable to accept the quote due to an error.... See below',
                    'pantit': 'acq',
                    'dispq': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Failed',
                    'restart':'yes'

                })
            if incom_post_acq is True:
                dispq = False
                return render(request, 'beanstalk_exe.html', {
                    'Req_data': 'Cannot convert to policy due to an error.... See below',
                    'pantit': 'ctp',
                    'dispq': dispq,
                    'Resp_data': Resp_data,
                    'stat': 'Failed',
                    'restart':'yes'

                })
        else:
            pass


    else:
        startmon = Monprocess('crq')
        crq_dat = startmon.procdata()
        print("type of create_quote data:",type(crq_dat))
        return render(request, 'beanstalk_exe.html',
                      {
                          'Req_data': crq_dat,
                          'pantit':'crq'
                      })


def con_gatepro(api_req,request,func):
    do_req = api_req
    funcp = func
    head = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    if funcp == 'cr_quote':
        response = requests.post("http://19289iisjnb001v/Quotes/quotes", data=do_req, headers=head)
    elif funcp == 'ac_quote':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/acceptpolicy", data=do_req, headers=head)
    elif funcp == 'conv_to_pol':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/policies", data=do_req, headers=head)
    elif funcp == 'amend_quote':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/policies", data=do_req, headers=head)
    elif funcp == 'acdec_amend':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Policies/acceptpolicyamendment", data=do_req, headers=head)
    else:
        context_dict = {'text': 'API Gateway testing channel - TAG'}
        return render(request, 'tag_home.html', context_dict)

    print("Response  from API Gateway...........", response.status_code)
    do_resp = response.json()
    do_resp = json.dumps(do_resp, indent=5)
    print(do_resp)
    print("Type of response data:", type(do_resp))
    return do_resp


def con_gatepro_get(reqn,func,request):
    gfunc = func
    vreqp = reqn

    if gfunc == 'view_policy':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.get("http://19289iisjnb001v/Policies/policies/"+vreqp+"/200/100/1", headers=head)
        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)
        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp
    else:
        pass




@login_required
def beanstalk_policy(request):
    if request.method == 'POST':
        selected_policy = request.POST.get('psel')

        #offline process - amend
        """
        amdata = offline_adder(selected_policy)
        return render(request, 'beanstalk_amendment.html',{
            "amd_data":amdata,
            "pantit": "amq"
        })"""
        #offline ends
        amdpol = Policy_starter('amend_policy')
        amdata = amdpol.get_quote(selected_policy)

        return render(request, 'beanstalk_amendment.html',{
            "amd_data":amdata,
            "pantit": "amq"
        })
    else:
        pass

    startpol = Policy_starter("get_policy")
    policy_list = startpol.policy_base()
    return render(request, 'beanstalk_exe2.html',{"polist":policy_list})


def beanstalk_asset(request):

    try:
        assert request.method == 'POST'
        motor_sel = request.POST.getlist("motor[]")
        content_sel = request.POST.getlist("content[]")
        allrisk_sel = request.POST.getlist("allrisk[]")

        print(motor_sel)
        print(content_sel)
        print(allrisk_sel)

        try:

            assert (motor_sel != [] or content_sel != [] or allrisk_sel != [])

            aops = asset_manager()
            motord = aops.get_vehicles('get_vehicle', motor_sel)

            asset_dict = {
                            'motor_list':motord,
                            'content_list':content_sel,
                            'allrisk_list':allrisk_sel
                         }

            asset_api_req = aops.asset_composer(asset_dict)

            return render(request, 'beanstalk_asset_quoting.html',{'pantit':'crq','Req_data':asset_api_req})

        except:
            asset_error = {"asset_error" : "You cannot execute the API without adding any assets.."}
            return render(request,'beanstalk_asset_home.html',asset_error)


    except:

        return render(request, 'beanstalk_asset_home.html')


def asset_execution(request):
    global asset_rrl

    # ENTERING CREATE QUOTE

    try:
        assert request.method == 'POST' and request.POST.get('crpost')

        alog = log_builder('asset_api')
        logger = alog.set_log('INFO', 'noformat')

        logger.info('CREATE QUOTE LOG ---------')
        logger.info('API Request(Asset API):--')

        asset_req = request.POST.get('content')
        logger.info(asset_req)
        gops = gateway_process('asset_api')
        asset_resp = gops.api_exec(asset_req)

        logger.info('API Response(Asset API):--')

        asset_resp = json.loads(asset_resp)

        if asset_resp:
            try:
                assert asset_resp['quoteNumber']
                aquotn = asset_resp['quoteNumber']

                asset_resp = json.dumps(asset_resp, indent=5)

                logger.info(asset_resp)
                asset_rrl = alog.return_file()

                #get Calculate prodata quote....
                aops = asset_manager()
                accept_q = aops.calculate_prorata(aquotn)

                return render(request, 'beanstalk_asset_quoting.html', {
                                                                         'pantit': 'acq',
                                                                         'Resp_data': asset_resp,
                                                                         'dispq':aquotn,
                                                                         'Req_data':accept_q,
                                                                         'stat':'success'
                                                                       })
            except:

                asset_resp = json.dumps(asset_resp, indent=5)

                logger.info(asset_resp)
                asset_rrl = alog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'crq',
                    'Resp_data':asset_resp,
                    'Req_data': 'Error in processing your quote. Please see the below response from API Gateway',
                    'stat': 'fail'
                })

    except:
        pass

    # ENTERING ACCEPT QUOTE

    try:
        assert request.method == 'POST' and request.POST.get('acpost')

        accept_req = request.POST.get('content')

        gops = gateway_process('calculate_prorata')
        accept_resp = gops.api_exec(accept_req)

        clog = log_builder('asset_api_calcpror')
        logger = clog.set_log('INFO', 'noformat')
        logger.info('CALCULATE PRORATA LOG ---------')
        logger.info('API Request(Asset API):--')

        logger.info(accept_req)

        logger.info('API Response(Asset API):--')

        accept_resp = json.loads(accept_resp)
        print("json loads ok")
        print(accept_resp['referenceNumber'])

        if accept_resp:
            try:
                assert accept_resp['referenceNumber']
                aquotr = accept_resp['referenceNumber']

                accept_resp = json.dumps(accept_resp, indent=5)

                logger.info(accept_resp)
                asset_rrl = clog.return_file()

                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit':'ctp',
                    'Resp_data': accept_resp,
                    'dispq': aquotr,
                    'go_conv':'go',
                    'stat': 'success'
                })
            except:

                accept_resp = json.dumps(accept_resp, indent=5)

                logger.info(accept_resp)
                asset_rrl = clog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'acq',
                    'Resp_data': accept_resp,
                    'Req_data': 'Error while accept quoting. Please see the below response from API Gateway',
                    'stat': 'fail'
                })

    except:
        pass

    # ENTERING CONVERT QUOTE TO POLICY

    try:
        assert request.method == 'POST' and request.POST.get('ctpost')

        policy_n = request.POST.get('convtop')
        print(policy_n)

        gops = gateway_process("convert_to_policy")
        conv_resp = gops.convtop_exec(policy_n)

        dlog = log_builder('asset_api_conv_to_policy_')
        logger = dlog.set_log('INFO', 'noformat')
        logger.info('CONVERT TO POLICY LOG ---------')
        logger.info('API Request(Asset API):--')

        logger.info(policy_n)

        logger.info('API Response(Asset API):--')

        conv_resp = json.loads(conv_resp)

        if conv_resp:
            try:
                assert conv_resp['policyNumber']
                aquotr = conv_resp['policyNumber']

                conv_resp = json.dumps(conv_resp, indent=5)

                logger.info(conv_resp)
                asset_rrl = dlog.return_file()

                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'ctp',
                    'Resp_data': conv_resp,
                    'dispq': aquotr,
                    'go_conv':'complete',
                    'stat': 'success'
                })
            except:

                conv_resp = json.dumps(conv_resp, indent=5)

                logger.info(conv_resp)
                asset_rrl = dlog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'ctp',
                    'Resp_data': conv_resp,
                    'go_conv': 'go',
                    'Req_data': 'Error while accept quoting. Please see the below response from API Gateway',
                    'stat': 'fail'
                })

    except:
        pass

@login_required
def beanstalk_amendment(request):
    global view_before
    global view_after
    global amdp
    incom_post_amq = False
    incom_post_adp = False

    if request.method == 'POST':
        ampost = request.POST.get('amdpost')
        adpost = request.POST.get('aacpost')
        vtpost = request.POST.get('vtrpost')

        print(ampost)

        if ampost is not None:
            # offline ends
            incom_post = ampost
            amd_req = request.POST.get('content')
            amd_req = json.loads(amd_req)
            view_pol = amd_req['PolicyNumber']
            print("Posted...",incom_post)
        elif adpost is not None:
            incom_post = adpost
            incom_decsn = request.POST.get('adsel')
        elif vtpost is not None:
            incom_post = vtpost
        else:
            pass


        if incom_post == 'PROCEED WITH POLICY AMENDMENT':
            view_before = con_gatepro_get(view_pol, request, 'view_policy')
            presp_data = con_gatepro(amd_req, request, 'amend_quote')
            incom_post_amq = True
        elif incom_post == 'PROCEED WITH THIS DECISION':
            startmon = Policy_starter('acdec_amend')
            acd_reqdata = startmon.accept_amendment(amdp,incom_decsn)
            presp_data = con_gatepro(acd_reqdata, request, 'acdec_amend')
            incom_post_adp = True
        elif incom_post == 'VIEW CHANGES':
            view_before = con_gatepro_get(view_pol, request, 'view_policy')
            incom_post_vtr = True
            return render(request, 'beanstalk_transition.html', {
                'bview_data': view_before,
                'aview_data':view_after
            })
        else:
            pass


        prdata = json.loads(presp_data)
        print(prdata)
        print(type(prdata))
        #req_bankd = json.loads(amd_req)




        if prdata['bSuccess'] is True:
            if incom_post_amq is True:
                amdp = prdata['QuoteNumber']
                print("...............INSIDE AMEND PROCESS AND ACCEPT/DECLINE RETURN............................")
                return render(request, 'beanstalk_amendment.html', {
                    'pantit': 'aac',
                    'dispq': amdp,
                    'Resp_data': presp_data,
                    'stat': 'Success'
                })
            if incom_post_adp is True:
                return render(request, 'beanstalk_amendment.html', {
                    'pantit': 'comp',
                    'dispq': amdp,
                    'Resp_data': presp_data,
                    'stat': 'Success'
                })
        elif prdata['bSuccess'] is False:
            context_dict = {'text': 'API Gateway testing channel - TAG'}
            return render(request, 'tag_home.html', context_dict)
    else:
        context_dict = {'text': 'API Gateway testing channel - TAG'}
        return render(request, 'tag_home.html', context_dict)


def tag_user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                goahead = 'userin'
                return HttpResponseRedirect(reverse(index))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Login failed against the below user details")
            lresp = 'invalid login details supplied!. Please retry or contact your admin'
            return render(request,'tag_login.html',{"eresp":lresp})
    else:
        return render(request,'tag_login.html',{})


def tag_register(request):

    registered = False

    if request.method == "POST":
        user_form = Userform(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = Userform()

    return render(request,'tag_register.html', {'user_form':user_form,
                                                'registered':registered})




@login_required
def special(request):
    return  HttpResponse("You are logged in, Nice!")


@login_required
def tag_user_logout(request):
    logout(request)
    return render(request,'tag_login.html')


def log_policy(quotes,policy_n,tuser):
    logpol = Policy_starter("log_policy")
    logpol.policy_log(tuser,policy_n,quotes)


def offline_pro(quotes,request):
    startoff = Composer('policy_hub')
    startoff.load_man(quotes)


def offline_adder(selectp):
    startadd = Composer('policy_hub')
    startadd.perform_tokens()
    amdata = startadd.amendpro(selectp)
    return amdata




