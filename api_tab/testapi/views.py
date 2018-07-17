from django.shortcuts import render
from .forms import Respform,Reqform
import json
from .mprocess import Monprocess
from .nprocess import Policy_starter
import requests
from .offline_composer import Composer
# Create your views here.

def index(request):
    context_dict = {'text': 'API GATEWAY TESTING CHANNEL - TAG'}
    return render(request, 'tag_home.html',context_dict)


def beanstalk_home(request):
    return render(request, 'beanstalk_home.html')


def beanstalk_quote(request):
    #reqf_obj = Reqform()
    #respf_obj = Respform()
    global startmon
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
        elif incom_post == 'PROCEED WITH GENERATE QUOTE':
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
        if rdata['bSuccess'] is True & incom_post_crq is not False:
            global dispq
            dispq = rdata['QuoteNumber']
            get_bankd = startmon.acq_bankupd(req_bankd)
            startmon = Monprocess('acq')
            acq_dat = startmon.acq_procdata(get_bankd,dispq)
            print("...............INSIDE CREATE PROCESS AND ACCEPT RETURN............................")
            return render(request, 'beanstalk_exe.html', {
                                                    'Req_data' : acq_dat,
                                                    'pantit' : 'acq',
                                                    'dispq':dispq,
                                                    'Resp_data':Resp_data,
                                                    'stat':'Success'
                                                   })
        elif rdata['bSuccess'] is True & incom_post_acq is not False:
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
        elif rdata['bSuccess'] is True & incom_post_ctq is not False:
            dispq = req_bankd['QuoteNumber']
            #startmon = Monprocess('ctp')
            #ctp_dat = startmon.ctp_procdata(dispq)
            log_policy(dispq,"tester")
            print("...............INSIDE CONVERT PROCESS PROCESS AND DONE............................")
            return render(request, 'beanstalk_exe.html', {
                'Req_data': '',
                'pantit': 'ctp',
                'dispp': dispq,
                'Resp_data': Resp_data,
                'stat': 'Success'
            })
        else:
            context_dict = {'text': 'API Gateway testing channel - TAG'}
            return render(request, 'tag_home.html', context_dict)

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

    if funcp == 'cr_quote':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/quotes", data=do_req, headers=head)
        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)
        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp
    elif funcp == 'ac_quote':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/acceptpolicy", data=do_req, headers=head)
        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)
        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp
    elif funcp == 'conv_to_pol':
        head = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        response = requests.post("http://19289iisjnb001v/Quotes/policies", data=do_req, headers=head)
        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)
        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp
    else:
        context_dict = {'text': 'API Gateway testing channel - TAG'}
        return render(request, 'tag_home.html', context_dict)

def beanstalk_policy(request):
    if request.method == 'POST':
        selected_policy = request.POST.get('psel')

        #offline process - amend

        amdata = offline_adder(selected_policy)
        return render(request, 'beanstalk_amendment.html',{
            "amd_data":amdata,
            "pantit": "amq"
        })
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


def log_policy(policy_n,tuser):
    logpol = Policy_starter("log_policy")
    logpol.policy_log(tuser,policy_n)


def offline_pro(quotes,request):
    startoff = Composer('policy_hub')
    startoff.load_man(quotes)


def offline_adder(selectp):
    startadd = Composer('policy_hub')
    startadd.perform_tokens()
    amdata = startadd.amendpro(selectp)
    return amdata