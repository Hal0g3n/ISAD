<template>
    <div class = "CDT"> <transition name=fade mode=out-in>

        <v-container v-if="!ready" key="Prep">
            <h1>Test Requirements</h1>
            For this test, you will require:
            <li>Audio Capture Device (e.g. Microphone)</li>
            <v-btn class=primary @click="()=>ready=true">Ready!</v-btn>
        </v-container>

        
        
        <v-container v-else key="CDT">
            <h1 class="subheading grey--text">Verbal Fluency Test</h1>

            Say as many unique animal names in 60 seconds. <br/>
            You only have <b>1</b> attempt. <br/>
            Press the button to begin!

            <center>
                <AudioRecorder @result="upload"/>
            </center>

        </v-container>

    </transition> </div>
</template>



<script>
import Vue from "vue";
import AudioRecorder from "@/components/AudioRecorder.vue";
import axios from "axios";
import { API } from "@/model/Data";

const api = API.getInstance();

export default Vue.extend({
    components: { AudioRecorder },

    data: () => ({
        ready: false,
    }),

    methods: { 
        upload(recording) {
            var form = new FormData();
            form.append("gender", api.gender);
            form.append("age", api.age);
            form.append("education", api.edu);
            form.append("mp3", recording);

            axios.post("http://127.0.0.1:5000/predict", form).then(
                (result) => { console.log(result); }, 
                (error) => { console.log(error); }
            );

            this.$emit("complete","Results");
        }
    },
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