<template>
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
</template>4>
        </div>
    </div>
</template>

<script>
// import { getTotalsNumber } from '@/endpoints/Totals'
import axios from 'axios';

export default {
    props:['totalsFirst'],
    data() {
        return{
            totals:[],
        }
    },

    methods:{}

}
</script>

<style scoped>
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
</style>