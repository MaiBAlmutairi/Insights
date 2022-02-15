<template>
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
</template>

<script>
import { Component, Vue, Prop } from 'vue-property-decorator';

import { getTotalsNumber } from '@/endpoints/Totals'
import axios from 'axios';

export default {
    props:['startDate','endDate'],

    
    data() {
        return{
            totals:[],
            // startDateF:this.startDate,
            // endDateF:this.endDate

//   testArr:[]
        }
    },

    methods:{
        listTotalsNumbers() {
            console.log(this.startDate, '  ' , this.endDate)
        const path = 'http://localhost:5000/dashboard/?fdate=' + this.startDate + '&ldate=' + this.endDate;
        axios.get(path)
            .then((res) => {
            //res.data.cards
            this.totals = [
                {name:"Total Transaction", mada:res.data.cards[0].span[0][0], masterCard:res.data.cards[2].master[0][0], visa:res.data.cards[1].visa[0][0]},
                {name:"Total Amount", mada:res.data.cards[0].span[0][1], masterCard:res.data.cards[2].master[0][1], visa:res.data.cards[1].visa[0][1]},
                {name:"Total Fees", mada:res.data.cards[0].span[0][2], masterCard:res.data.cards[2].master[0][2], visa:res.data.cards[1].visa[0][2]},
                {name:"Total VAT", mada:res.data.cards[0].span[0][3], masterCard:res.data.cards[2].master[0][3], visa:res.data.cards[1].visa[0][3]},
                {name:"Payable Amount", mada:res.data.cards[0].span[0][4], masterCard:res.data.cards[2].master[0][4], visa:res.data.cards[1].visa[0][4]},
            ]
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        },
    },

    mounted() {
        // this.testFun()
        this.listTotalsNumbers()
    }
}
</script>

<style scoped>
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
</style>