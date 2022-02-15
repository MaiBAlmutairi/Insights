<template>
<div>
 <h1>Admin Home</h1>
  <div class="filter">
        <div class="startDate">
          <date-picker v-model="startDate"></date-picker>
        </div>
        <div class="EndDate">
          <date-picker v-model="endDate"></date-picker>
      </div>
      <div class="termanil">
        <multiselect v-model="selectMerchant" :options="merchantlist" :searchable="false" :close-on-select="true" :show-labels="false" placeholder="select merchant" label="merchant" track-by="merchant" @input="listTerminalsList"></multiselect>
      </div>

      <div class="termanil">
        <multiselect v-model="selectTerminal" :options="terminalsList" :searchable="false" :close-on-select="true" :show-labels="false" placeholder="select terminalid" label="terminal" track-by="terminal" @input="listMerchantlist"></multiselect>
      </div>

      <button @click="setFilter">Refresh</button>
  </div>

  <div class="filterTypeAndDay">
    <div class="selected"><multiselect  v-model="selectTypeSelect" :options="typeSelect" :close-on-select="true" :clear-on-select="true" :preserve-search="true" placeholder="Pick some" @input="dataGraph"></multiselect></div>
    <div class="btns">
        <button @click="filterDay(1)" :class="dayActive">Day</button>
        <button @click="filterDay(2)"  :class="weeklyActive">Weekly</button>
        <button @click="filterDay(3)" :class="monthlyActive">Monthly</button>
    </div>
  </div>

  <div class="graph">
    <apexchart height="300" type="bar" :options="options" :series="series"></apexchart>
  </div>

  <!-- <TotalsNumbers :startDate="startDate" :endDate="endDate" ref="callFunTotalsNumbers"/> -->
    <div class="totals">
        <div class="logoPayment">
            <img src="@/assets/mada.png" alt="logo" />
            <img src="@/assets/masterCard.png" alt="logo" />
            <img src="@/assets/visaCard.png" alt="logo" />
        </div>
        <div class="total" v-for="total in totals" :key="total">
            <h5>{{total.name}}</h5>
            <h4>{{total.mada}}</h4>
            <hr>
            <h4>{{total.masterCard}}</h4>
            <hr>
            <h4>{{total.visa}}</h4>
        </div>
    </div>


    <div class="previousDueAmount">
      <span>Previous Due Amount <span v-if="totalPay[0].payValue != null">{{totalPay[0].payValue}}</span><span v-if="totalPay[0].payValue == null">0</span></span>
      <span>Total Payable Amount <span v-if="totalPay[1].payValue != null">{{totalPay[1].payValue}}</span><span v-if="totalPay[1].payValue == null">0</span></span>
      <span>Total Misc Charges <span v-if="totalPay[2].payValue != null">{{totalPay[2].payValue}}</span><span v-if="totalPay[2].payValue == null">0</span></span>
    </div>
    <hr>

    <div class="previousDueAmount">
      <span>Total Paid Amount <span v-if="totalPay[3].payValue != null">{{totalPay[3].payValue}}</span><span v-if="totalPay[3].payValue == null">0</span></span>
      <span>Total Due Amount <span v-if="totalPay[4].payValue != null">{{totalPay[4].payValue}}</span><span v-if="totalPay[4].payValue == null">0</span></span>
    </div>


        <button class="export" @click="exportToExcel">Export To Excel</button>



    <div>
        <data-table v-bind="bindings"/>
    </div>
</div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import TotalsNumbers from '@/components/HomePage/TotalsNumbers.vue';
// import { getTotalsNumber } from '@/endpoints/Totals';
import Multiselect from 'vue-multiselect'

import axios from 'axios';

 import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import moment from 'moment'


@Component({
  components: {
    TotalsNumbers,
    DatePicker,
    Multiselect
  },
    computed: {
        bindings() {
            return {
                columns: [
                    {
                        key: "AmountTotal",
                    },
                    {
                        key: "CustomerID",
                    },
                    {
                        key: "MerchantName",
                    },
                    {
                        key: "PaymentTransferID",
                    },
                    {
                        key: "PaymentTransferStatusID",
                    },
                    {
                        key: "TotalTransactionAmount",
                    },
                    {
                        key: "TransferAmount",
                    },
                    {
                        key: "TransferDate",
                    },
                ],
                data: this.dataValue
                /* other props...*/
            }
        }
    },
})


export default class AdminHome extends Vue {
      typeSelect:any = ['Amount (SAR)', 'Count']
      selectTypeSelect:any = ''

      columnsDate:any = []
      dataValue:any = []

      period:any = 'daily'
      dayActive:any = 'dayActive'
      weeklyActive:any = ''
      monthlyActive:any = ''

      startDate:any = ''
      endDate:any = ''

      totals:any = []
      totalPay:any = []
      terminals:any = [
        {id: 1, city_name:"city1"}
      ]
      selectTerminal:any = ''
      terminalsList:any = []

      selectMerchant:any = ''
      merchantlist:any = []
      
      options:any = {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: []
        }
      }
      // series:any = [{
      //     name: 'series-1',
      //     data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
      //   },  
      // ]

      series:any = []


      async listMerchantlist() {
        let tid
        if(this.selectTerminal == '' || this.selectTerminal == null){
          tid = null
        }else{
          tid = this.selectTerminal.terminal
        }
        const path = 'http://localhost:5000/merchantlist/?tid='+tid;
        await axios.get(path)
            .then((res) => {
            //res.data.cards

            this.merchantlist = res.data

            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        }

      async listTerminalsList() {
        let merc
        if(this.selectMerchant == '' || this.selectMerchant == null){
          merc = null
        }else{
          merc = this.selectMerchant.merchant
        }
        
        const path = 'http://localhost:5000/terminallist/?cid='+ merc;
        await axios.get(path)
            .then((res) => {
            //res.data.cards

            this.terminalsList = res.data

            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        }



        async listTotalsNumbers() {
          let FormatStartDate
          let FormatEndDate
          if(this.startDate == ''){
            FormatStartDate = null
          }else{
            FormatStartDate = moment(this.startDate).format('YYYY-MM-DD');
          }

          if(this.endDate == ''){
            FormatEndDate = null
          }else{
            FormatEndDate = moment(this.endDate).format('YYYY-MM-DD');
          } 
          

        let tid
        if(this.selectTerminal == '' || this.selectTerminal == null){
          tid = null
        }else{
          tid = this.selectTerminal.terminal
        }

          
            console.log( FormatStartDate, '  ' , FormatEndDate)
        const path = 'http://localhost:5000/dashboard/?fdate=' + FormatStartDate + '&ldate=' + FormatEndDate + '&tid=' + tid;
        await axios.get(path)
            .then((res) => {
            //res.data.cards
            this.totals = [
                {name:"Total Transaction", mada:res.data.cards[0].span[0][0], masterCard:res.data.cards[2].master[0][0], visa:res.data.cards[1].visa[0][0]},
                {name:"Total Amount", mada:res.data.cards[0].span[0][1], masterCard:res.data.cards[2].master[0][1], visa:res.data.cards[1].visa[0][1]},
                {name:"Total Fees", mada:res.data.cards[0].span[0][2], masterCard:res.data.cards[2].master[0][2], visa:res.data.cards[1].visa[0][2]},
                {name:"Total VAT", mada:res.data.cards[0].span[0][3], masterCard:res.data.cards[2].master[0][3], visa:res.data.cards[1].visa[0][3]},
                {name:"Payable Amount", mada:res.data.cards[0].span[0][4], masterCard:res.data.cards[2].master[0][4], visa:res.data.cards[1].visa[0][4]},
            ]

            //console.log("EEEEEEEEEEEEEEEEEEEEEEEE>> " + res.data.cards[3].prev_due[0][0])

            this.totalPay = [
                {"payValue":res.data.cards[3].prev_due[0][0]},
                {"payValue":res.data.cards[4].total_pay[0][0]},
                {"payValue":res.data.cards[5].total_misc[0][0]},
                {"payValue":res.data.cards[6].total_paid[0][0]},
                {"payValue":res.data.cards[7].total_due[0][0]}
            ]



            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        }

      setFilter() {
        this.listTotalsNumbers()
        this.dataGraph()
        // alert("DDD")
        // console.log("DDDDD")
        // setTimeout( () => this.$refs.callFunTotalsNumbers.listTotalsNumbers, 0)
      }




      async dataGraph() {
        let fDate
        let lDate
        let mode = 'amount'
        let period = 'daily'
        let tid

        let FormatStartDate = moment(this.startDate).format('YYYY-MM-DD');
        let FormatEtartDate = moment(this.endDate).format('YYYY-MM-DD');


        if(this.startDate == ''){
          fDate = null
        }else{
          fDate = FormatStartDate
        }

        if(this.endDate == ''){
          lDate = null
        }else{
          lDate = FormatEtartDate
        }
        
        if(this.selectTerminal == '' || this.selectTerminal == null){
          tid = null
        }else{
          tid = this.selectTerminal.terminal
        }

        if(this.selectTypeSelect == 'Amount (SAR)'){
          mode = 'amount'
        }else if(this.selectTypeSelect == 'Count'){
          mode = "count"
        }else if(this.selectTypeSelect == null || this.selectTypeSelect == ''){
          mode = 'amount'
        }
        
        
        let arrayGraphAmount = []

        const path = 'http://localhost:5000/graph/?fdate=' + fDate + '&ldate=' + lDate + '&mode=' + mode + '&period=' + this.period + '&tid=' + tid;
        await axios.get(path)
            .then((res) => {
            //res.data.cards

            //this.merchantlist = res.data

      // series:any = [{
      //   name: 'Net Profit',
      //   data: [44, 55, 57, 56, 61, 58, 63, 60, 66]
      // }, {
      //   name: 'Revenue',
      //   data: [76, 85, 101, 98, 87, 105, 91, 114, 94]
      // }, {
      //   name: 'Free Cash Flow',
      //   data: [35, 41, 36, 26, 45, 48, 52, 53, 41]
      // }]


            if(mode == 'amount'){
              let categoriesdata=[]
              let settleddata=[]
              let unsettleddata=[]
              res.data.map(x => {
              categoriesdata.push(x.date)
              settleddata.push(x.settled)
              unsettleddata.push(x.unsettled)
              this.options = {xaxis:{categories:categoriesdata}}

                arrayGraphAmount = [{
                  "name": "settled",
                  "data": settleddata
                },{
                  "name": "unsettled",
                  "data": unsettleddata
                }
                ]
              })

              this.series = arrayGraphAmount
            }else if(mode == 'count'){
              let categoriesdata =[]
              let countdata = []
              res.data.map(x => {
              categoriesdata.push(x.date)
              countdata.push(x.count)
                this.options = {xaxis:{categories:categoriesdata}}

                arrayGraphAmount = [{
                  "name": "count",
                  "data": countdata
                }]
              })
              this.series = arrayGraphAmount

            }

            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        }

      filterDay(id:any){
        if(id == 1){
          
          this.period = 'daily'
          this.dataGraph()

          this.dayActive = 'dayActive'
          this.weeklyActive = ''
          this.monthlyActive = ''
        }else if(id == 2){
          this.period = 'weekly'
          this.dataGraph()

          this.dayActive = ''
          this.weeklyActive = 'weeklyActive'
          this.monthlyActive = ''
        }else if(id == 3){
          this.period = 'monthly'
          this.dataGraph()

          this.dayActive = ''
          this.weeklyActive = ''
          this.monthlyActive = 'monthlyActive'
        }
      }
      async dataTable() {
        const path = 'http://127.0.0.1:5000/paymenttable/';
        await axios.get(path)
            .then((res) => {
            //res.data.cards

            // this.terminalsList = res.data
             res.data.map(x => {
               this.dataValue.push({"AmountTotal": x.AmountTotal, "CustomerID": x.CustomerID, "MerchantName": x.MerchantName, "PaymentTransferID": x.PaymentTransferID, "PaymentTransferStatusID": x.PaymentTransferStatusID, "TotalTransactionAmount": x.TotalTransactionAmount, "TransferAmount": x.TransferAmount, "TransferDate": x.TransferDate})
            })
            

            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        }


        exportToExcel() {
            fetch('http://127.0.0.1:5000/exportpayment/')
                .then((response) => response.blob())
                .then((blob) => {
                saveAs(blob, 'export Table');
                });
        }
        

      
    mounted() {
        // this.testFun()
        this.listTotalsNumbers()
        this.listMerchantlist()
        this.listTerminalsList()

        this.dataGraph()
        this.dataTable()
    }
    
}
</script>

<style scoped>
.filter{
  width:100%;
  height:60px;
  background:#FFF;
  box-shadow:0 0 5px rgba(0,0,0,.13);
  border-radius:5px;
  padding:15px 3%;
  margin-bottom:40px;
}

.filter .startDate,
.filter .EndDate{
  float:left;
  margin-right:2%;
}



.filter button{
  width:100px;
  height:35px;
  background:blueviolet;
  border-radius:5px;
  float:left;
  border:0;
  outline:none;
  color:#FFF;
  font-weight:bold;
  cursor:pointer;
}




.totals{
    min-height:400px;
}
.logoPayment{
    width:6%;
    height:95px;
    float:left;
    margin-right:3%;
    padding-top:43px;
}

.logoPayment img{
    width:100%;
    height:auto;
    margin-bottom:10px;
}

.total{
    width:17%;
    height:185px;
    background:#5f27cd;
    float: left;
    margin-right:1%;
    border-radius:5px;
}
.total:last-child{
    margin-right:0
}


.total h5{
    text-align:center;
    color:#FFF;
    margin-top:5px;
    magin-bottom:10px
}
.total hr{
    display:block;
    width:40%;
    height:2px;
    background:#FFF;
    margin:auto;
    border:0;
    margin:10px auto
}
.total h4{
    margin:0;
    text-align:center;
    color:#FFF;
    font-size:20px;
    font-weight:bold;
}

.termanil{
  width:15%;
  float:left;
  margin-right:2%;
}

.graph{
  clear:both;
  width:100%;
}

.selected{
  width:30%;
  float:left;
  clear:both;
}

.btns{
  width:50%;
  float:right;
}

.btns button{
  border:0;
  background:#b5b5b5;
  color:#FFF;
  border-radius:5px;
  width:25%;
  height:35px;
}

.btns button:nth-of-type(2){
  margin:0 2%;
}

.dayActive{
  background: #5f27cd;
}
.weeklyActive{
  background: #5f27cd;
}
.monthlyActive{
  background: #5f27cd;
}



.previousDueAmount{
  margin-bottom:50px;
}

.previousDueAmount >span{
  font-size:15px;
  font-weight:bold;
  margin-right:4%;
  /* margin-bottom:40px; */
}

.previousDueAmount span span{
  margin-left:5%;
  color:blue;
  font-size:20px;
}


.export{
border: 0;
    width: 17%;
    height: 45px;
    color: #FFF;
    background: blue;
    font-weight:bold;
    display:block;
    margin:20px auto;

}
</style>