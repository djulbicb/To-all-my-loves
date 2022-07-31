
import mongoose from "mongoose";

//const Schema = mongoose.Schema;
const { Schema } = mongoose;

const goalSchema = new Schema({
    text: String
})

const Goal = mongoose.model('Goal', goalSchema);

export default Goal;