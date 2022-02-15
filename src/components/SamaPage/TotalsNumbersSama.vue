<template>
    <div class="totals">
        <div class="total" v-for="total in totals" :key="total">
            <h5>{{total.name}}</h5>
            <h4>{{total.totalNumber}}</h4>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return{
            totals:[],
        }
    },

    methods:{
        listTotalsNumbers() {
        const path = 'http://localhost:5000/samadashboard';
        axios.get(path)
            .then((res) => {
                this.totals = [
                    {name:"Value of transactions", totalNumber:res.data[0][0]},
                    {name:"Number of Active Merchants", totalNumber:res.data[1][0]},
                    {name:"Contactless Transactions", totalNumber:"NA"},
                    {name:"Number of Active Terminals", totalNumber:res.data[2][0]},
                    {name:"Registered Merchant", totalNumber:res.data[3][0]},
                    {name:"Number of Transactions", totalNumber:res.data[4][0]},
                ]
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
        },
    },

    mounted() {
        this.listTotalsNumbers()
    }

}
</script>

<style scoped>
.totals{
    min-height:400px;
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
</style>