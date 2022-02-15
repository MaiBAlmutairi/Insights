from os import name
from flask import Flask, request
from flask.json import jsonify
from flask import Response
from flask_caching import Cache
import simplejson as json
from decimal import Decimal
import pandas as pd
import pypyodbc
cache=Cache()    
from flask_cors import CORS
from flask_cors import cross_origin
app = Flask(__name__)
app.config['CACHE_TYPE']='simple'
cache.init_app(app)
cors = CORS(app, resources={r"/*":{'Access-Control-Allow-Origin':"*"}})
connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-OC0HNEM\SQLEXPRESS;Database=MmsAPI;uid=Mai;pwd=Uohb@2171;MARS_Connection=yes')

def execute(query):
        connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-OC0HNEM\SQLEXPRESS;Database=MmsAPI;uid=Mai;pwd=Uohb@2171;MARS_Connection=yes')

        cursor = connection.cursor()
        cursor.execute(query)
        result=cursor.fetchall()

        cursor.close()
        connection.close()
        return result

@app.route('/firstoperationdashboard/',methods=["GET"])
@cross_origin()
def firstoperation():
    fdate = request.args.get('fdate')
    ldate = request.args.get('ldate')
    
    if((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')):
        total_transaction="SELECT COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        total_transaction_val="SELECT CONVERT(int,ROUND(sum(TransactionAmount),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        vat_val="SELECT CONVERT(int,ROUND(sum(VatAmount),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        Additional_Fee="SELECT CONVERT(int,ROUND(sum(Additional_Fee),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        bank_Fee="SELECT CONVERT(int,ROUND(sum(BankFee),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        aggregator_Fee="SELECT CONVERT(int,ROUND(sum(AggregatorFee),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"

    else:
        total_transaction=f"SELECT COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        total_transaction_val=f"SELECT CONVERT(int,ROUND(sum(TransactionAmount),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        vat_val=f"SELECT CONVERT(int,ROUND(sum(VatAmount),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        Additional_Fee=f"SELECT CONVERT(int,ROUND(sum(Additional_Fee),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        bank_Fee=f"SELECT CONVERT(int,ROUND(sum(BankFee),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        aggregator_Fee=f"SELECT CONVERT(int,ROUND(sum(AggregatorFee),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"

    #cursor.execute(total_transaction)
    tot_transaction=execute(total_transaction)
    #cursor.execute(total_transaction_val)
    tot_transaction_val=execute(total_transaction_val)
    #cursor.execute(vat_val)
    vat_amount=execute(vat_val)
    #cursor.execute(Additional_Fee)
    add_fees=execute(Additional_Fee)
    #cursor.execute(bank_Fee)
    bank_Fees=execute(bank_Fee)
    #cursor.execute(aggregator_Fee)
    aggr_Fees=execute(aggregator_Fee)
    #cursor.execute(misc_charges)
    misc_charges=execute(misc_charges)

    firstoperation = [
    {name:'tot_transaction',
    'value':tot_transaction[0][0]
    },
    {name:'tot_transaction_val',
    'value':tot_transaction_val[0][0]
    },
    {name:'vat_amount',
    'value':vat_amount[0][0]
    },
    {name:'add_fees',
    'value':add_fees[0][0]
    },
    {name:'bank_Fees',
    'value':bank_Fees[0][0]    
    },
    {name:'aggr_Fees',
    'value':aggr_Fees[0][0]    
    },
    {name:'misc_charges',
    'value':misc_charges[0][0]    
    },     
    ]   
    return  jsonify(firstoperation)

@app.route('/secondoperationdashboard/',methods=["GET"])
@cross_origin()

def secondoperation():
    fdate = request.args.get('fdate')
    ldate = request.args.get('ldate')
    #cursor = connection.cursor()
    if((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')):
        cust_pay_amount="SELECT CONVERT(int,ROUND(sum(PaidAmount+UnpaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        cust_paid_amount="SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        cust_due_amount="SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        bank_recieved=f"SELECT CONVERT(int,ROUND(sum(TransferAmount),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"
        bank_recievable=f"SELECT CONVERT(int,ROUND(sum(Actual_AmountToTransfer),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"
        bank_due=f"SELECT CONVERT(int,ROUND(sum(TransferAmount-Actual_AmountToTransfer),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"
        top_up=f"SELECT CONVERT(int,ROUND(sum(Actual_AmountToTransfer-TransferAmount),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"

    else:
        cust_pay_amount=f"SELECT CONVERT(int,ROUND(sum(PaidAmount+UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"
        cust_paid_amount=f"SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"
        cust_due_amount=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"        
        bank_recieved=f"SELECT CONVERT(int,ROUND(sum(TransferAmount),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
        bank_recievable=f"SELECT CONVERT(int,ROUND(sum(Actual_AmountToTransfer),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
        bank_due=f"SELECT CONVERT(int,ROUND(sum(TransferAmount-Actual_AmountToTransfer),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
        top_up=f"SELECT CONVERT(int,ROUND(sum(Actual_AmountToTransfer-TransferAmount),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
    #cursor.execute(cust_pay_amount)
    cust_pay_amount=execute(cust_pay_amount)
    #cursor.execute(cust_paid_amount)
    cust_paid_amount=execute(cust_paid_amount)
    #cursor.execute(cust_due_amount)
    cust_due_amount=execute(cust_due_amount)
    #cursor.execute(bank_recieved)
    bank_recieved=execute(bank_recieved)
    #cursor.execute(bank_recievable)
    bank_recievable=execute(bank_recievable)
    #cursor.execute(bank_due)
    bank_due=execute(bank_due)
    #cursor.execute(top_up)
    top_up=execute(top_up)


    secondoperation = [
    {name:'cust_pay_amount',
    'value':cust_pay_amount[0][0]
    },
    {name:'cust_paid_amount',
    'value':cust_paid_amount[0][0]
    },
    {name:'cust_due_amount',
    'value':cust_due_amount[0][0]
    },
    {name:'bank_recievable',
    'value':bank_recievable[0][0]
    },
    {name:'bank_recieved',
    'value':bank_recieved[0][0]    
    },
    {name:'bank_due',
    'value':bank_due[0][0]    
    },
    {name:'top_up',
    'value':top_up[0][0]    
    },     
    ]   
    return  jsonify(secondoperation)

    
@app.route('/samadashboard', methods=["GET"]) 
@cross_origin()
@cache.cached(timeout=600)
def sama():
    #cursor = connection.cursor()
    #cursor.execute("SELECT CONVERT(int,ROUND(sum(TransactionAmount),0)) FROM dbo.TransactionDetails")
    result1=execute("SELECT CONVERT(int,ROUND(sum(TransactionAmount),0)) FROM dbo.TransactionDetails")
    #cursor.execute("SELECT COUNT(distinct MerchantID) FROM dbo.TransactionDetails where DateDiff(D, TransactionDate, GetDate()) < 31")
    result2=execute("SELECT COUNT(distinct MerchantID) FROM dbo.TransactionDetails where DateDiff(D, TransactionDate, GetDate()) < 31")
    #cursor.execute("SELECT COUNT(distinct TerminalID) FROM dbo.TransactionDetails where DateDiff(D, TransactionDate, GetDate()) < 31")
    result3=execute("SELECT COUNT(distinct TerminalID) FROM dbo.TransactionDetails where DateDiff(D, TransactionDate, GetDate()) < 31")
    #cursor.execute("SELECT COUNT(distinct MerchantID) FROM dbo.TransactionDetails")
    result4=execute("SELECT COUNT(distinct MerchantID) FROM dbo.TransactionDetails")
    #cursor.execute("SELECT COUNT(TransSeqNumber) FROM dbo.TransactionDetails")
    result5=execute("SELECT COUNT(TransSeqNumber) FROM dbo.TransactionDetails")       
    return Response(json.dumps(result1+result2+result3+result4+result5))
@app.route('/merchantlist/',methods=["GET"])
@cross_origin()

def merchant():
    #cursor = connection.cursor()
    terminal = request.args.get('tid')
    if(terminal=='all'):
        terminal='null'
    if (terminal=='null' or terminal==None):
        merchantlist="select MerchantName from Terminals"
    else:
        merchantlist=f"select DISTINCT MerchantName from Terminals WHERE TerminalID = {terminal}"
    #cursor.execute(merchantlist)
    results=execute(merchantlist)
    output = [{'merchant':'all'}]
    content = {}
    for result in results:
       content = {'merchant': result[0]}
       output.append(content)
       content = {}
    response=jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/terminallist/',methods=["GET"])
@cross_origin()

def terminal():
    #cursor = connection.cursor()
    merchant=request.args.get('cid')
    if(merchant=='all'):
        merchant='null'
    if (merchant=='null' or merchant==None):
        terminallist="select DISTINCT TerminalID from Terminals"
    else:
        terminallist=f"select DISTINCT TerminalID from Terminals WHERE MerchantName = '{merchant}'"
    #cursor.execute(terminallist)
    results=execute(terminallist)
    output = [{'terminal':'all'}]
    content = {}
    for result in results:
       content = {'terminal': result[0]}
       output.append(content)
       content = {}
    response=jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/graph/', methods=["GET"])
@cross_origin()

def graph():

    #cursor = connection.cursor()
    tid = request.args.get('tid')
    fdate = request.args.get('fdate')
    ldate = request.args.get('ldate')
    mode=request.args.get('mode')
    period=request.args.get('period')

    if (mode=='count'):
        if (period=='daily'):
            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TransactionDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(d,TransactionDate,GETDATE()) <= 6 GROUP BY TransactionDate ORDER BY TransactionDate"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                    query=f"SELECT TransactionDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(d,TransactionDate,GETDATE()) <= 6 AND TerminalID='{tid}' GROUP BY TransactionDate ORDER BY TransactionDate"

            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):

                query=f"SELECT TOP(7) TransactionDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY TransactionDate ORDER BY TransactionDate"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):

                    query=f"SELECT TOP(7) TransactionDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'  GROUP BY TransactionDate ORDER BY TransactionDate"
                
        elif (period=='weekly'):
            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT WeekOfYear,WeekSundayDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails  WHERE DATEDIFF(DAY,getdate(),TransactionDate) <= 31 AND MONTH(getdate())-MONTH(TransactionDate)<=1 AND YEAR(getdate())=YEAR(TransactionDate) GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT WeekOfYear,WeekSundayDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(d,TransactionDate,GETDATE()) <= 31 AND MONTH(getdate())-MONTH(TransactionDate)<=1 AND YEAR(getdate())=YEAR(TransactionDate) AND TerminalID='{tid}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TOP(4) WeekOfYear,WeekSundayDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT TOP(4) WeekOfYear,WeekSundayDate,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"

        elif (period=='monthly'):

            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT FirstDayOfMonth,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) <= 12 GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT FirstDayOfMonth,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) <= 12 AND TerminalID='{tid}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"

            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TOP(12) FirstDayOfMonth,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT TOP(12) FirstDayOfMonth,COUNT(TransSeqNumber) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"

    elif (mode=='amount'):
        if (period=='daily'):
            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TransactionDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(d,TransactionDate,GETDATE()) <= 6 GROUP BY TransactionDate ORDER BY TransactionDate"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                    query=f"SELECT TransactionDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(d,TransactionDate,GETDATE()) <= 6 AND TerminalID='{tid}' GROUP BY TransactionDate ORDER BY TransactionDate"

            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):

                query=f"SELECT TOP(7) TransactionDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY TransactionDate ORDER BY TransactionDate"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):

                    query=f"SELECT TOP(7) TransactionDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'  GROUP BY TransactionDate ORDER BY TransactionDate"
                
        elif (period=='weekly'):
            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT WeekOfYear,WeekSundayDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(DAY,getdate(),TransactionDate) <= 31 AND MONTH(getdate())-MONTH(TransactionDate)<=1 AND YEAR(getdate())=YEAR(TransactionDate) GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekSundayDate"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT WeekOfYear,WeekSundayDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(DAY,GETDATE(),TransactionDate()) <= 31 AND MONTH(GETDATE())=MONTH(TransactionDate) AND YEAR(GETDATE())=YEAR(TransactionDate) AND TerminalID='{tid}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekSundayDate"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TOP(4) WeekOfYear,WeekSundayDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT TOP(4) WeekOfYear,WeekSundayDate,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}' GROUP BY WeekOfYear,WeekSundayDate ORDER BY WeekOfYear"

        elif (period=='monthly'):

            if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT FirstDayOfMonth,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(MONTH,TransactionDate,GETDATE()) <= 12 GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"
            elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT FirstDayOfMonth,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) <= 12 TerminalID='{tid}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"

            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):
                query=f"SELECT TOP(12) FirstDayOfMonth,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"
            elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null' or tid!=None)):
                query=f"SELECT TOP(12) FirstDayOfMonth,SUM(SettledAmount),SUM(TransactionAmount-SettledAmount) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}' GROUP BY FirstDayOfMonth ORDER BY FirstDayOfMonth"

    results=execute(query)
    output = []
    if (period=='daily' and mode == 'count'):           
            content = {}
            for result in results:
                content = {'date': result[0], 'count': result[1]}
                output.append(content)
                content = {}
    elif (period=='weekly' and mode == 'count'):           
            content = {}
            for result in results:
                content = {'week': result[0], 'date': result[1],'count':result[2]}
                output.append(content)
                content = {}
    elif (period=='monthly' and mode == 'count'):           
            content = {}
            for result in results:
                content = {'date': result[0],'count':result[1]}
                output.append(content)
                content = {}
    elif (period=='daily' and mode == 'amount'):           
            content = {}
            for result in results:
                content = {'date': result[0], 'settled': result[1],'unsettled': result[2]}
                output.append(content)
                content = {}
    elif (period=='weekly' and mode == 'amount'):           
            content = {}
            for result in results:
                content = {'week': result[0], 'date': result[1], 'settled': result[2],'unsettled': result[3]}
                output.append(content)
                content = {}
    elif (period=='monthly' and mode == 'amount'):           
            content = {}
            for result in results:
                content = {'date': result[0],'settled': result[1],'unsettled': result[2]}
                output.append(content)
                content = {}
    response=jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route('/exportoperation/',methods=["GET"])
@cross_origin()

def exportoperation():
    query="SELECT CardScheme as CardScheme,sum(BankFee) as BankFee,sum(AggregatorFee) as AggregatorFee FROM TransactionDetails GROUP BY CardScheme"
    P_data = pd.read_sql_query(query, connection)
    P_data.to_excel('operation.xlsx')
    return  jsonify({
            'status': 200})
@app.route('/aggregator/',methods=["GET"])
@cross_origin()

def aggreagator():
    #cursor = connection.cursor()
    query="SELECT CardScheme as CardScheme,sum(BankFee) as BankFee,sum(AggregatorFee) as AggregatorFee FROM TransactionDetails GROUP BY CardScheme"
    #cursor.execute(query)
    results=execute(query)
    content = {}
    output = []
    for result in results:
        content = {'CardScheme': result[0],'BankFee': int(result[1]),'AggregatorFee': int(result[2])}
        output.append(content)
        content = {}
    response=jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
@app.route('/exportpayment/',methods=["GET"])
@cross_origin()

def exportpayment():
    query="SELECT p.PaymentTransferID as RefID,p.TransferDate as Date,p.CustomerID as CustomerID,m.MerchantName as CustomerName,m.TotalTransactionAmount as TotalTransaction,p.Reversed_Amount+p.ReversedTotalTx as MiscDeduction,p.TransferAmount as Amount,p.PaymentTransferStatusID as Status FROM PaymentTransfers p ,Merchants m WHERE p.CustomerID=m.CustomerID"
    P_data = pd.read_sql_query(query, connection)
    P_data.to_excel('payments.xlsx')
    return  jsonify({
            'status': 200})
@app.route('/paymenttable/', methods=["GET"])
@cross_origin()

def paymenttable():
    #cursor = connection.cursor()
    query="SELECT p.PaymentTransferID,p.TransferDate,p.CustomerID,m.MerchantName,m.TotalTransactionAmount,p.Reversed_Amount+p.ReversedTotalTx,p.TransferAmount,p.PaymentTransferStatusID FROM PaymentTransfers p ,Merchants m WHERE p.CustomerID=m.CustomerID"
    #cursor.execute(query)
    results=execute(query)
    content = {}
    output = []
    for result in results:
        content = {'PaymentTransferID': result[0],'TransferDate': result[1],'CustomerID': result[2],'MerchantName': result[3],'TotalTransactionAmount': int(result[4]),'AmountTotal': int(result[5]),'TransferAmount': int(result[6]),'PaymentTransferStatusID':result[7]}
        output.append(content)
        content = {}
    response=jsonify(output)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/dashboard/', methods=["GET"])
@cross_origin()

def home():

    #cursor = connection.cursor()
    tid = request.args.get('tid')
    fdate = request.args.get('fdate')
    ldate = request.args.get('ldate')
    if(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid=='all' or tid=='null' or tid==None)):
        
        span_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='SPAN' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"    
        visa_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='VISA Credit' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        master_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='MasterCard' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        total_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        prev_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) > 0"
        total_pay_query=f"SELECT CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        total_paid_query=f"SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"

    elif(((fdate==None and ldate==None) or (fdate=='null' and ldate=='null')) and (tid!='all' or tid!='null')):
        
        span_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='SPAN' AND TerminalID='{tid}' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"    
        visa_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='VISA Credit' AND TerminalID='{tid}' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        master_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='MasterCard' AND TerminalID='{tid}' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        total_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE TerminalIDs='{tid}' AND DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        prev_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE TerminalIDs='{tid}' AND DATEDIFF(m,UpdatedDate,GETDATE()) > 0"
        total_pay_query=f"SELECT CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE TerminalID='{tid}' AND DATEDIFF(m,TransactionDate,GETDATE()) = 0"
        total_paid_query=f"SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE TerminalIDs='{tid}' AND DATEDIFF(m,UpdatedDate,GETDATE()) = 0"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE DATEDIFF(m,TransferDate,GETDATE()) = 0"

    elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid=='all' or tid=='null' or tid==None)):
        span_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='SPAN' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"    
        visa_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='VISA Credit' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"   
        master_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='MasterCard' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        total_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"    
        prev_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"
        total_pay_query=f"SELECT CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}'"
        total_paid_query=f"SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}'"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
    elif(((fdate!=None and ldate!=None) or (fdate!='null' and ldate!='null')) and (tid!='all' or tid!='null')):
        span_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='SPAN' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'"    
        visa_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='VISA Credit' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'"   
        master_query=f"SELECT COUNT(TransSeqNumber),ROUND(sum(TransactionAmount),0),CONVERT(int,ROUND(sum(AggregatorFee+Additional_Fee+MerchantFee+BankFee),0)),CONVERT(int,ROUND(sum(VatAmount),0)),CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE CardScheme='MasterCard' AND TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'"
        total_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}' AND UpdatedDate<='{ldate}' AND TerminalIDs='{tid}'"    
        prev_due_query=f"SELECT CONVERT(int,ROUND(sum(UnpaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate<'{fdate}' AND TerminalIDs='{tid}'"
        total_pay_query=f"SELECT CONVERT(int,ROUND(sum(NetAmount),0)) FROM dbo.TransactionDetails WHERE TransactionDate>='{fdate}' AND TransactionDate<='{ldate}' AND TerminalID='{tid}'"
        total_paid_query=f"SELECT CONVERT(int,ROUND(sum(PaidAmount),0)) FROM dbo.Merchants WHERE UpdatedDate>='{fdate}' AND UpdatedDate<='{ldate}' AND TerminalIDs='{tid}'"
        misc_charges=f"SELECT CONVERT(int,ROUND(sum(Adjustment_Amount),0)) FROM dbo.PaymentTransfers WHERE TransferDate>='{fdate}' AND TransferDate<='{ldate}'"
   
    #cursor.execute(span_query)
    SPANresult=execute(span_query)
    #cursor.execute(visa_query)
    VISAresult=execute(visa_query)
    #cursor.execute(master_query)
    MASTERresult=execute(master_query)
    #cursor.execute(total_due_query)
    total_due=execute(total_due_query)
    #cursor.execute(prev_due_query)
    prev_due=execute(prev_due_query) 
    #cursor.execute(total_pay_query)
    total_pay=execute(total_pay_query)
    #cursor.execute(total_paid_query)
    total_paid=execute(total_paid_query) 
    total_misc=execute(misc_charges) 
    cards = [
    {
    'span':SPANresult
    },
    {
    'visa':VISAresult
    },
    {
    'master':MASTERresult
    },
    {
    'prev_due':prev_due
    },
    {
    'total_pay':total_pay
    },
    {
    'total_misc':total_misc
    },
    {
    'total_paid':total_paid    
    },
    {
    'total_due':total_due
    },     
    ]   

    response=jsonify({
            'status': 200,
            'cards': cards
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
if __name__ == '__main__':

    app.debug = True
    app.run(use_reloader=True)

