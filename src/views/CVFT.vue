<template>
    <div class = "CDT"> <transition name=fade mode=out-in>

        <v-container v-if="!ready" key="Prep">
            <h1>Test Requirements</h1>
            For this test, you will require:
            <li>A Microphone (Most devices have 1)</li>
            <v-btn class="primary" style="margin-top:3vmin" @click="()=>ready=true">Ready!</v-btn>
        </v-container>

        
        
        <v-container v-else key="CDT">
            <h1>Verbal Fluency Test</h1>

            Say as many unique animal names in 60 seconds. <br/>
            You only have <b>1</b> attempt. <br/>
            Press the button to begin! <br>

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
import { data } from "@/model/Data";

export default Vue.extend({
    components: { AudioRecorder },

    data: () => ({
        ready: false,
    }),

    methods: { 
        upload(recording) {
            var form = new FormData();
            form.append("gender", data.gender);
            form.append("age", data.age);
            form.append("education", data.edu);
            form.append("audio", recording.blob, "audio");

            // Indicate Test exists
            data.scores["Verbal Test"] = -1;

            // Post Request
            axios.post("https://pearson.pythonanywhere.com/predict", form).then(
                (result) => data.scores = {...data.scores, "Verbal Test": result.data.response * 100}, 
                (error) => console.log(error),
            );

            // State its completion
            this.$emit("complete");
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