<template>
    <div class = "Intro"> 
        <transition name="fade" mode='out-in'>
            <center v-if="show == 0">
                <img class=ma-10 style="height:50vmin; width=50vmin" src="@/assets/logo.svg"/>
                
                <p class="text-h6" style="font-size:1rem">
                    Intelligent Screening for Alzheimer's Disease
                    A simple 10 minute test to check for Alzheimer's.<br> <br>
                    A project by Vikram Ramanathan, James Sng and Yap Yuan Xi
                </p>

                <v-btn class=primary @click="show = 1">Take the Test</v-btn>
            </center>

            <!-- Get user information -->
            <Info v-else-if="show == 1" @complete="show = 2"/>

            <!-- Get test to perform -->
            <Selection v-else @selected="$emit('complete')"/>
            
        </transition>
    </div>
</template>



<script>
import Vue from "vue";
import Info from "@/views/Info.vue";
import Selection from "@/views/Selection.vue";
import {data} from "@/model/Data";

export default Vue.extend({
    data: () => ({show: 0, api: data}),
    components: {Info, Selection},
});

</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>