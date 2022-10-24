<template>
    <div class = "CDT"> <transition name=fade mode=out-in>
        <v-container v-if="!ready" key="Prep">
            <h1>Requirements</h1>
            For this test, you will require:
            <li>Blank White Paper</li>
            <li>Your device's camera</li>
            <v-btn class="primary" style="margin-top:3vmin" @click="()=>ready=true">Ready!</v-btn>
        </v-container>

        <v-container v-else key="CDT">
            <h1>Drawing Test</h1>

            <div style="font-size:1rem" class=my-1>
            Draw and Upload an analog clock. <br>
            The clock should show 10 past 11. <br>
            Give yourself 3 minutes to draw. <br>
            </div>

            <center>

                <ImageChooser 
                    name="image-chooser" 
                    displayName="Upload Clock Image" 
                    @change="uploadFile" 
                    :error="error" 
                    :progress="progress" 
                    style="height:50vmin; width:50vmin;"
                    :baseSrc="image"
                    />

            </center>

        </v-container>

    </transition> </div>
</template>



<script>
import Vue from "vue";
import ImageChooser from "@/components/ImageChooser.vue";
import axios from "axios";
import { data } from "@/model/Data";

export default Vue.extend({
    components: {ImageChooser},
    data: () => ({
        ready: false,
        progress: null,
        error: null,
        image: null
    }),
    methods: {
        uploadFile(file) {
            // Checks if file is actually an image
            if (file.file.type.substring(0, 5) != "image") {
                this.error = "File is not an image";
                return;
            }

            // Nullify the error
            this.error = null;
            
            // Simple animation
            this.progress = 0;
            var anim = setInterval(() => {
                if (this.progress >= 100) {
                    this.progress == null;
                    clearInterval(anim);
                }
                else this.progress += 1;
            }, 10);


            // Prepare post request
            var form = new FormData();
            form.append("filename", file.file.name);
            
            // Indicate Test exists
            data.scores["Drawing Test"] = -1;

            // Go and fetch the result
            axios.post("https://pearson.pythonanywhere.com/predict2", form).then(
                (result) => {  
                    data.scores = {...data.scores, "Drawing Test": result.data.response * 100};
                    clearInterval(anim);
                }, 
                (error) => console.log(error),
            );

            // Completed test
            this.$emit("complete");
        }
    }
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