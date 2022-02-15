<template>
    <div class="samaPage">
        <h2>Operation Dashboard</h2>

        <div class="filter">
                <div class="startDate">
                <date-picker v-model="startDate"></date-picker>
                </div>
                <div class="EndDate">
                <date-picker v-model="endDate"></date-picker>
            </div>
            <button @click="setFilter">Refresh</button>
        </div>

        <!--<TotalsTransactionalOverview  :totalsFirst="totalsFirst"/>-->
    <div class="totals">
        <h3>Transactional Overview</h3>
        <div class="total">
            <!-- <h5>Total Transaction</h5> -->
            <h5>{{totalsFirst[0].name}}</h5>
            <h4 v-if="totalsFirst[0].value == null">0</h4>
            <h4 v-if="totalsFirst[0].value != null">{{totalsFirst[0].value}}</h4>
        </div>
        <div class="total">
            <!-- <h5>Total Transaction Value</h5> -->
            <h5>{{totalsFirst[1].name}}</h5>
            <h4 v-if="totalsFirst[1].value == null">0</h4>
            <h4 v-if="totalsFirst[1].value != null">{{totalsFirst[1].value}}</h4>
        </div>
    </div>
        <!--<TotalsFeeOverview  :totalsFirst="totalsFirst"/> -->

    <div class="totals">
        <h3>Fee Overview</h3>
        <div class="total">
            <!-- <h5>VAT</h5> -->
            <h5>{{totalsFirst[2].name}}</h5>
            <h4 v-if="totalsFirst[2].value == null">0</h4>
            <h4 v-if="totalsFirst[2].value != null">{{totalsFirst[2].value}}</h4>
        </div>
        <div class="total">
            <!-- <h5>Additional Fee</h5> -->
            <h5>{{totalsFirst[3].name}}</h5>
            <h4 v-if="totalsFirst[3].value == null">0</h4>
            <h4 v-if="totalsFirst[3].value != null">{{totalsFirst[3].value}}</h4>        </div>
        <div class="total">
            <!-- <h5>Total Bank Fee</h5> -->
            <h5>{{totalsFirst[4].name}}</h5>
            <h4 v-if="totalsFirst[4].value == null">0</h4>
            <h4 v-if="totalsFirst[4].value != null">{{totalsFirst[4].value}}</h4>        </div>
        <div class="total">
            <!-- <h5>Aggregator Fee</h5> -->
            <h5>{{totalsFirst[5].name}}</h5>
            <h4 v-if="totalsFirst[5].value == null">0</h4>
            <h4 v-if="totalsFirst[5].value != null">{{totalsFirst[5].value}}</h4>        </div>
        <div class="total">
            <!-- <h5>Miscellaneous Charges</h5> -->
            <h5>{{totalsFirst[6].name}}</h5>
            <h4 v-if="totalsFirst[6].value == null">0</h4>
            <h4 v-if="totalsFirst[6].value != null">{{totalsFirst[6].value}}</h4>             
        </div>
    </div>

      <!-- <CustomerPaymentOverview  :totalsSecond="totalsSecond"/>-->

    <div class="totals">
        <h3>Customer Payment Overview</h3>
        <div class="total">
            <!-- <h5>Customer Payable amount</h5> -->
            <h5>{{totalsSecond[0].name}}</h5>
            <h4 v-if="totalsSecond[0].value == null">0</h4>
            <h4 v-if="totalsSecond[0].value != null">{{totalsSecond[0].value}}</h4>
        </div>
        <div class="total">
            <!-- <h5>Custom Paid Amount</h5> -->
            <h5>{{totalsSecond[1].name}}</h5>
            <h4 v-if="totalsSecond[1].value == null">0</h4>
            <h4 v-if="totalsSecond[1].value != null">{{totalsSecond[1].value}}</h4>        </div>
        <div class="total">
            <!-- <h5>Custom Due Amount</h5> -->
            <h5>{{totalsSecond[2].name}}</h5>
            <h4 v-if="totalsSecond[2].value == null">0</h4>
            <h4 v-if="totalsSecond[2].value != null">{{totalsSecond[2].value}}</h4>        </div>
    </div>

       <!--  <PTSOverview :totalsSecond="totalsSecond"/>-->
    <div class="totals">
        <h3>PTS Overview</h3>
        <div class="total">
            <h5>{{totalsSecond[3].name}}</h5>
            <h4 v-if="totalsSecond[3].value == null">0</h4>
            <h4 v-if="totalsSecond[3].value != null">{{totalsSecond[3].value}}</h4>
        </div>
        <div class="total">
            <h5>{{totalsSecond[4].name}}</h5>
            <h4 v-if="totalsSecond[4].value == null">0</h4>
            <h4 v-if="totalsSecond[4].value != null">{{totalsSecond[4].value}}</h4>        </div>
        <div class="total">
            <h5>{{totalsSecond[5].name}}</h5>
            <h4 v-if="totalsSecond[5].value == null">0</h4>
            <h4 v-if="totalsSecond[5].value != null">{{totalsSecond[5].value}}</h4>        </div>
        <div class="total">
            <h5>{{totalsSecond[6].name}}</h5>
            <h4 v-if="totalsSecond[6].value == null">0</h4>
            <h4 v-if="totalsSecond[6].value != null">{{totalsSecond[6].value}}</h4>        </div>
    </div>
         

    
        <button class="export" @click="exportToExcel">Export To Excel</button>



        <div>
            <data-table v-bind="bindings"/>
        </div>

    </div>
</template>

<script>
import { Component, Vue, Prop } from 'vue-property-decorator';

import TotalsTransactionalOverview from '@/components/OperationPage/TotalsTransactionalOverview.vue'
import TotalsFeeOverview from '@/components/OperationPage/TotalsFeeOverview.vue'
import CustomerPaymentOverview from '@/components/OperationPage/CustomerPaymentOverview.vue'
import PTSOverview from '@/components/OperationPage/PTSOverview.vue'
import axios from 'axios';

import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import moment from 'moment'

export default {
    components:{
        TotalsTransactionalOverview,
        TotalsFeeOverview,
        CustomerPaymentOverview,
        PTSOverview,
        DatePicker
    },

    computed: {
        bindings() {
            return {
                columns: [
                    {
                        key: "CardScheme",
                    },
                    {
                        key: "BankFee",
                    },
                    {
                        key: "AggregatorFee",
                    },
                ],
                data: this.dataValue
                /* other props...*/
            }
        }
    },

    data() {
        return{
            startDate:'',
            endDate:'',
            totalsFirst:[],
            totalsSecond:[],
            dataValue: []
        }
    },

    methods:{

        getTotals() {
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
            const path = 'http://localhost:5000/firstoperationdashboard/?fdate=' + FormatStartDate + '&ldate=' + FormatEndDate;
            axios.get(path)
                .then((res) => {
                //res.data.cards
                let totalsFirst = []
              res.data.map(x => {
                totalsFirst.push({
                  "name": x.nt,
                  "value": x.value
                })
              })
              this.totalsFirst = totalsFirst
              console.log(this.totalsFirst)


            


                // this.totalsFirst = [
                //     {name:"Total Transaction", value:res.data[0].firstoperation[0].tot_transaction[0][0]},
                //     {name:"Total Transaction Value", value:res.data[1].firstoperation[0].tot_transaction_val[0][0]},
                //     {name:"VAT", value:res.data[2][0].firstoperation[0].vat_amount[0][0]},
                //     {name:"Additional Fee", value:res.data[3].firstoperation[0].add_fees[0][0]},
                //     {name:"Total Bank Fee", value:res.data[4].firstoperation[0].bank_Fees[0][0]},
                //     {name:"Aggregator Fee", value:res.data[5].firstoperation[0].aggr_Fees[0][0]},
                //     {name:"Miscellaneous Charges", value:res.data[6].firstoperation[0].misc_charges[0][0]},
                //     // {name:"Custom Paid Amount", value:res.data[7][0]},
                //     // {name:"Custom Due Amount", value:res.data[8][0]},
                // ]
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });


            const path2 = 'http://localhost:5000/secondoperationdashboard/?fdate=' + FormatStartDate + '&ldate=' + FormatEndDate;
            axios.get(path2)
                .then((res) => {
                //res.data.cards
                let totalsSecond = []
                res.data.map(x => {
                   totalsSecond.push({
                    "name": x.nt,
                    "value": x.value
                    })
                })
                console.log("DDDDDDDDDDDDDDDDD >>>> " + this.totalsSecond)
                 this.totalsSecond = totalsSecond

                // this.totalsSecond = [
                //     {name:"Customer Payable amount", value:res.data[0].secondoperation[0].cust_pay_amount[0][0]},
                //     {name:"Custom Paid Amount", value:res.data[1].secondoperation[0].cust_paid_amount[0][0]},
                //     {name:"Custom Due Amount", value:res.data[2][0].secondoperation[0].cust_due_amount[0][0]},
                //     {name:"Bank Receivable Amount", value:res.data[3].secondoperation[0].bank_recievable[0][0]},
                //     {name:"Bank Received Amount", value:res.data[4].secondoperation[0].bank_recieved[0][0]},
                //     {name:"Bank Due Amount", value:res.data[5].secondoperation[0].bank_due[0][0]},
                //     {name:"Top up", value:res.data[6].secondoperation[0].top_up[0][0]}
                // ]
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
                });



        },

        setFilter() {
            this.getTotals()
        },

      async dataTable() {
        const path = 'http://127.0.0.1:5000/aggregator/';
        await axios.get(path)
            .then((res) => {
            //res.data.cards

            // this.terminalsList = res.data
             res.data.map(x => {
               this.dataValue.push({"AggregatorFee": x.AggregatorFee, "BankFee": x.BankFee, "CardScheme": x.CardScheme})
            })
            

            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        },

        exportToExcel() {
            fetch('http://127.0.0.1:5000/exportoperation/')
                .then((response) => response.blob())
                .then((blob) => {
                saveAs(blob, 'export Table');
                });
        }


        
    },

    mounted() {
        this.getTotals()
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
  margin-right:5%;
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
    background:#FFF;
    min-height:auto;
    box-shadow:0 0 5px rgba(0,0,0,.13);
    padding:20px 3%;
    overflow:hidden;
    margin-bottom:40px;
}

.totals h3{
    font-size:20px;
    font-weight:100;
    margin:0;
    margin-bottom:30px;
}

.total{
    width:15%;
    height:130px;
    background:#5f27cd;
    float: left;
    margin-right:2%;
    border-radius:5px;
}
.total:last-child{
    margin-right:0
}


.total h5{
    text-align:center;
    color:#FFF;
    margin-top:5px;
    margin-bottom:10px;
    height:40px;
    font-size:15px;
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
    font-size:15px;
    font-weight:bold;
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
