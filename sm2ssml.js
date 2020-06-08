const smd = require("speechmarkdown-js");

if (process.argv.length < 3) {
  console.log("Usage: node " + process.argv[1] + " FILENAME");
  process.exit(1);
}
var fs = require("fs");
try {
  filename = process.argv[2];
  var md = fs.readFileSync(filename, "utf8");
} catch (e) {
  console.log("Error:", e.stack);
}

const options = {
  platform: "google-assistant",
  includeParagraphTag: true
};

const speech = new smd.SpeechMarkdown();
const ssml = speech.toSSML(md, options);
console.log(ssml);
