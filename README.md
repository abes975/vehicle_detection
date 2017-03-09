<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8" />
      <title>writeup_template</title>
      <style>.markdown-preview:not([data-use-github-style]) { padding: 2em; font-size: 1.2em; color: rgb(171, 178, 191); overflow: auto; background-color: rgb(40, 44, 52); }
.markdown-preview:not([data-use-github-style]) > :first-child { margin-top: 0px; }
.markdown-preview:not([data-use-github-style]) h1, .markdown-preview:not([data-use-github-style]) h2, .markdown-preview:not([data-use-github-style]) h3, .markdown-preview:not([data-use-github-style]) h4, .markdown-preview:not([data-use-github-style]) h5, .markdown-preview:not([data-use-github-style]) h6 { line-height: 1.2; margin-top: 1.5em; margin-bottom: 0.5em; color: rgb(255, 255, 255); }
.markdown-preview:not([data-use-github-style]) h1 { font-size: 2.4em; font-weight: 300; }
.markdown-preview:not([data-use-github-style]) h2 { font-size: 1.8em; font-weight: 400; }
.markdown-preview:not([data-use-github-style]) h3 { font-size: 1.5em; font-weight: 500; }
.markdown-preview:not([data-use-github-style]) h4 { font-size: 1.2em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) h5 { font-size: 1.1em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) h6 { font-size: 1em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) strong { color: rgb(255, 255, 255); }
.markdown-preview:not([data-use-github-style]) del { color: rgb(124, 135, 156); }
.markdown-preview:not([data-use-github-style]) a, .markdown-preview:not([data-use-github-style]) a code { color: rgb(82, 139, 255); }
.markdown-preview:not([data-use-github-style]) img { max-width: 100%; }
.markdown-preview:not([data-use-github-style]) > p { margin-top: 0px; margin-bottom: 1.5em; }
.markdown-preview:not([data-use-github-style]) > ul, .markdown-preview:not([data-use-github-style]) > ol { margin-bottom: 1.5em; }
.markdown-preview:not([data-use-github-style]) blockquote { margin: 1.5em 0px; font-size: inherit; color: rgb(124, 135, 156); border-color: rgb(75, 83, 98); border-width: 4px; }
.markdown-preview:not([data-use-github-style]) hr { margin: 3em 0px; border-top: 2px dashed rgb(75, 83, 98); background: none; }
.markdown-preview:not([data-use-github-style]) table { margin: 1.5em 0px; }
.markdown-preview:not([data-use-github-style]) th { color: rgb(255, 255, 255); }
.markdown-preview:not([data-use-github-style]) th, .markdown-preview:not([data-use-github-style]) td { padding: 0.66em 1em; border: 1px solid rgb(75, 83, 98); }
.markdown-preview:not([data-use-github-style]) code { color: rgb(255, 255, 255); background-color: rgb(58, 63, 75); }
.markdown-preview:not([data-use-github-style]) pre.editor-colors { margin: 1.5em 0px; padding: 1em; font-size: 0.92em; border-radius: 3px; background-color: rgb(49, 54, 63); }
.markdown-preview:not([data-use-github-style]) kbd { color: rgb(255, 255, 255); border-width: 1px 1px 2px; border-style: solid; border-color: rgb(75, 83, 98) rgb(75, 83, 98) rgb(62, 68, 81); background-color: rgb(58, 63, 75); }
.markdown-preview[data-use-github-style] { font-family: "Helvetica Neue", Helvetica, "Segoe UI", Arial, freesans, sans-serif; line-height: 1.6; word-wrap: break-word; padding: 30px; font-size: 16px; color: rgb(51, 51, 51); overflow: scroll; background-color: rgb(255, 255, 255); }
.markdown-preview[data-use-github-style] > :first-child { margin-top: 0px !important; }
.markdown-preview[data-use-github-style] > :last-child { margin-bottom: 0px !important; }
.markdown-preview[data-use-github-style] a:not([href]) { color: inherit; text-decoration: none; }
.markdown-preview[data-use-github-style] .absent { color: rgb(204, 0, 0); }
.markdown-preview[data-use-github-style] .anchor { position: absolute; top: 0px; left: 0px; display: block; padding-right: 6px; padding-left: 30px; margin-left: -30px; }
.markdown-preview[data-use-github-style] .anchor:focus { outline: none; }
.markdown-preview[data-use-github-style] h1, .markdown-preview[data-use-github-style] h2, .markdown-preview[data-use-github-style] h3, .markdown-preview[data-use-github-style] h4, .markdown-preview[data-use-github-style] h5, .markdown-preview[data-use-github-style] h6 { position: relative; margin-top: 1em; margin-bottom: 16px; font-weight: bold; line-height: 1.4; }
.markdown-preview[data-use-github-style] h1 .octicon-link, .markdown-preview[data-use-github-style] h2 .octicon-link, .markdown-preview[data-use-github-style] h3 .octicon-link, .markdown-preview[data-use-github-style] h4 .octicon-link, .markdown-preview[data-use-github-style] h5 .octicon-link, .markdown-preview[data-use-github-style] h6 .octicon-link { display: none; color: rgb(0, 0, 0); vertical-align: middle; }
.markdown-preview[data-use-github-style] h1:hover .anchor, .markdown-preview[data-use-github-style] h2:hover .anchor, .markdown-preview[data-use-github-style] h3:hover .anchor, .markdown-preview[data-use-github-style] h4:hover .anchor, .markdown-preview[data-use-github-style] h5:hover .anchor, .markdown-preview[data-use-github-style] h6:hover .anchor { padding-left: 8px; margin-left: -30px; text-decoration: none; }
.markdown-preview[data-use-github-style] h1:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h2:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h3:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h4:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h5:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h6:hover .anchor .octicon-link { display: inline-block; }
.markdown-preview[data-use-github-style] h1 tt, .markdown-preview[data-use-github-style] h2 tt, .markdown-preview[data-use-github-style] h3 tt, .markdown-preview[data-use-github-style] h4 tt, .markdown-preview[data-use-github-style] h5 tt, .markdown-preview[data-use-github-style] h6 tt, .markdown-preview[data-use-github-style] h1 code, .markdown-preview[data-use-github-style] h2 code, .markdown-preview[data-use-github-style] h3 code, .markdown-preview[data-use-github-style] h4 code, .markdown-preview[data-use-github-style] h5 code, .markdown-preview[data-use-github-style] h6 code { font-size: inherit; }
.markdown-preview[data-use-github-style] h1 { padding-bottom: 0.3em; font-size: 2.25em; line-height: 1.2; border-bottom: 1px solid rgb(238, 238, 238); }
.markdown-preview[data-use-github-style] h1 .anchor { line-height: 1; }
.markdown-preview[data-use-github-style] h2 { padding-bottom: 0.3em; font-size: 1.75em; line-height: 1.225; border-bottom: 1px solid rgb(238, 238, 238); }
.markdown-preview[data-use-github-style] h2 .anchor { line-height: 1; }
.markdown-preview[data-use-github-style] h3 { font-size: 1.5em; line-height: 1.43; }
.markdown-preview[data-use-github-style] h3 .anchor { line-height: 1.2; }
.markdown-preview[data-use-github-style] h4 { font-size: 1.25em; }
.markdown-preview[data-use-github-style] h4 .anchor { line-height: 1.2; }
.markdown-preview[data-use-github-style] h5 { font-size: 1em; }
.markdown-preview[data-use-github-style] h5 .anchor { line-height: 1.1; }
.markdown-preview[data-use-github-style] h6 { font-size: 1em; color: rgb(119, 119, 119); }
.markdown-preview[data-use-github-style] h6 .anchor { line-height: 1.1; }
.markdown-preview[data-use-github-style] p, .markdown-preview[data-use-github-style] blockquote, .markdown-preview[data-use-github-style] ul, .markdown-preview[data-use-github-style] ol, .markdown-preview[data-use-github-style] dl, .markdown-preview[data-use-github-style] table, .markdown-preview[data-use-github-style] pre { margin-top: 0px; margin-bottom: 16px; }
.markdown-preview[data-use-github-style] hr { height: 4px; padding: 0px; margin: 16px 0px; border: 0px none; background-color: rgb(231, 231, 231); }
.markdown-preview[data-use-github-style] ul, .markdown-preview[data-use-github-style] ol { padding-left: 2em; }
.markdown-preview[data-use-github-style] ul.no-list, .markdown-preview[data-use-github-style] ol.no-list { padding: 0px; list-style-type: none; }
.markdown-preview[data-use-github-style] ul ul, .markdown-preview[data-use-github-style] ul ol, .markdown-preview[data-use-github-style] ol ol, .markdown-preview[data-use-github-style] ol ul { margin-top: 0px; margin-bottom: 0px; }
.markdown-preview[data-use-github-style] li > p { margin-top: 16px; }
.markdown-preview[data-use-github-style] dl { padding: 0px; }
.markdown-preview[data-use-github-style] dl dt { padding: 0px; margin-top: 16px; font-size: 1em; font-style: italic; font-weight: bold; }
.markdown-preview[data-use-github-style] dl dd { padding: 0px 16px; margin-bottom: 16px; }
.markdown-preview[data-use-github-style] blockquote { padding: 0px 15px; color: rgb(119, 119, 119); border-left: 4px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] blockquote > :first-child { margin-top: 0px; }
.markdown-preview[data-use-github-style] blockquote > :last-child { margin-bottom: 0px; }
.markdown-preview[data-use-github-style] table { display: block; width: 100%; overflow: auto; word-break: keep-all; }
.markdown-preview[data-use-github-style] table th { font-weight: bold; }
.markdown-preview[data-use-github-style] table th, .markdown-preview[data-use-github-style] table td { padding: 6px 13px; border: 1px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] table tr { border-top: 1px solid rgb(204, 204, 204); background-color: rgb(255, 255, 255); }
.markdown-preview[data-use-github-style] table tr:nth-child(2n) { background-color: rgb(248, 248, 248); }
.markdown-preview[data-use-github-style] img { max-width: 100%; box-sizing: border-box; }
.markdown-preview[data-use-github-style] .emoji { max-width: none; }
.markdown-preview[data-use-github-style] span.frame { display: block; overflow: hidden; }
.markdown-preview[data-use-github-style] span.frame > span { display: block; float: left; width: auto; padding: 7px; margin: 13px 0px 0px; overflow: hidden; border: 1px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] span.frame span img { display: block; float: left; }
.markdown-preview[data-use-github-style] span.frame span span { display: block; padding: 5px 0px 0px; clear: both; color: rgb(51, 51, 51); }
.markdown-preview[data-use-github-style] span.align-center { display: block; overflow: hidden; clear: both; }
.markdown-preview[data-use-github-style] span.align-center > span { display: block; margin: 13px auto 0px; overflow: hidden; text-align: center; }
.markdown-preview[data-use-github-style] span.align-center span img { margin: 0px auto; text-align: center; }
.markdown-preview[data-use-github-style] span.align-right { display: block; overflow: hidden; clear: both; }
.markdown-preview[data-use-github-style] span.align-right > span { display: block; margin: 13px 0px 0px; overflow: hidden; text-align: right; }
.markdown-preview[data-use-github-style] span.align-right span img { margin: 0px; text-align: right; }
.markdown-preview[data-use-github-style] span.float-left { display: block; float: left; margin-right: 13px; overflow: hidden; }
.markdown-preview[data-use-github-style] span.float-left span { margin: 13px 0px 0px; }
.markdown-preview[data-use-github-style] span.float-right { display: block; float: right; margin-left: 13px; overflow: hidden; }
.markdown-preview[data-use-github-style] span.float-right > span { display: block; margin: 13px auto 0px; overflow: hidden; text-align: right; }
.markdown-preview[data-use-github-style] code, .markdown-preview[data-use-github-style] tt { padding: 0.2em 0px; margin: 0px; font-size: 85%; border-radius: 3px; background-color: rgba(0, 0, 0, 0.0392157); }
.markdown-preview[data-use-github-style] code::before, .markdown-preview[data-use-github-style] tt::before, .markdown-preview[data-use-github-style] code::after, .markdown-preview[data-use-github-style] tt::after { letter-spacing: -0.2em; content: " "; }
.markdown-preview[data-use-github-style] code br, .markdown-preview[data-use-github-style] tt br { display: none; }
.markdown-preview[data-use-github-style] del code { text-decoration: inherit; }
.markdown-preview[data-use-github-style] pre > code { padding: 0px; margin: 0px; font-size: 100%; word-break: normal; white-space: pre; border: 0px; background: transparent; }
.markdown-preview[data-use-github-style] .highlight { margin-bottom: 16px; }
.markdown-preview[data-use-github-style] .highlight pre, .markdown-preview[data-use-github-style] pre { padding: 16px; overflow: auto; font-size: 85%; line-height: 1.45; border-radius: 3px; background-color: rgb(247, 247, 247); }
.markdown-preview[data-use-github-style] .highlight pre { margin-bottom: 0px; word-break: normal; }
.markdown-preview[data-use-github-style] pre { word-wrap: normal; }
.markdown-preview[data-use-github-style] pre code, .markdown-preview[data-use-github-style] pre tt { display: inline; max-width: initial; padding: 0px; margin: 0px; overflow: initial; line-height: inherit; word-wrap: normal; border: 0px; background-color: transparent; }
.markdown-preview[data-use-github-style] pre code::before, .markdown-preview[data-use-github-style] pre tt::before, .markdown-preview[data-use-github-style] pre code::after, .markdown-preview[data-use-github-style] pre tt::after { content: normal; }
.markdown-preview[data-use-github-style] kbd { display: inline-block; padding: 3px 5px; font-size: 11px; line-height: 10px; color: rgb(85, 85, 85); vertical-align: middle; border-width: 1px; border-style: solid; border-color: rgb(204, 204, 204) rgb(204, 204, 204) rgb(187, 187, 187); border-radius: 3px; box-shadow: rgb(187, 187, 187) 0px -1px 0px inset; background-color: rgb(252, 252, 252); }
.markdown-preview[data-use-github-style] a { color: rgb(51, 122, 183); }
.markdown-preview[data-use-github-style] code { color: inherit; }
.markdown-preview[data-use-github-style] pre.editor-colors { padding: 0.8em 1em; margin-bottom: 1em; font-size: 0.85em; border-radius: 4px; overflow: auto; }
.scrollbars-visible-always .markdown-preview pre.editor-colors .vertical-scrollbar, .scrollbars-visible-always .markdown-preview pre.editor-colors .horizontal-scrollbar { visibility: hidden; }
.scrollbars-visible-always .markdown-preview pre.editor-colors:hover .vertical-scrollbar, .scrollbars-visible-always .markdown-preview pre.editor-colors:hover .horizontal-scrollbar { visibility: visible; }
.markdown-preview .task-list-item-checkbox { position: absolute; margin: 0.25em 0px 0px -1.4em; }
.spell-check-misspelling .region {
  border-bottom: 2px dotted rgba(255, 51, 51, 0.75);
}
.spell-check-corrections {
  width: 25em !important;
}

pre.editor-colors {
  background-color: #282c34;
  color: #abb2bf;
}
pre.editor-colors .line.cursor-line {
  background-color: rgba(153, 187, 255, 0.04);
}
pre.editor-colors .invisible {
  color: #abb2bf;
}
pre.editor-colors .cursor {
  border-left: 2px solid #528bff;
}
pre.editor-colors .selection .region {
  background-color: #3e4451;
}
pre.editor-colors .bracket-matcher .region {
  border-bottom: 1px solid #528bff;
  box-sizing: border-box;
}
pre.editor-colors .invisible-character {
  color: rgba(171, 178, 191, 0.15);
}
pre.editor-colors .indent-guide {
  color: rgba(171, 178, 191, 0.15);
}
pre.editor-colors .wrap-guide {
  background-color: rgba(171, 178, 191, 0.15);
}
pre.editor-colors .find-result .region.region.region,
pre.editor-colors .current-result .region.region.region {
  border-radius: 2px;
  background-color: rgba(82, 139, 255, 0.24);
  transition: border-color 0.4s;
}
pre.editor-colors .find-result .region.region.region {
  border: 2px solid transparent;
}
pre.editor-colors .current-result .region.region.region {
  border: 2px solid #528bff;
  transition-duration: .1s;
}
pre.editor-colors .gutter .line-number {
  color: #636d83;
  -webkit-font-smoothing: antialiased;
}
pre.editor-colors .gutter .line-number.cursor-line {
  color: #abb2bf;
  background-color: #2c313a;
}
pre.editor-colors .gutter .line-number.cursor-line-no-selection {
  background-color: transparent;
}
pre.editor-colors .gutter .line-number .icon-right {
  color: #abb2bf;
}
pre.editor-colors .gutter:not(.git-diff-icon) .line-number.git-line-removed.git-line-removed::before {
  bottom: -3px;
}
pre.editor-colors .gutter:not(.git-diff-icon) .line-number.git-line-removed::after {
  content: "";
  position: absolute;
  left: 0px;
  bottom: 0px;
  width: 25px;
  border-bottom: 1px dotted rgba(224, 82, 82, 0.5);
  pointer-events: none;
}
pre.editor-colors .gutter .line-number.folded,
pre.editor-colors .gutter .line-number:after,
pre.editor-colors .fold-marker:after {
  color: #abb2bf;
}
.syntax--comment {
  color: #5c6370;
  font-style: italic;
}
.syntax--comment .syntax--markup.syntax--link {
  color: #5c6370;
}
.syntax--entity.syntax--name.syntax--type {
  color: #e5c07b;
}
.syntax--entity.syntax--other.syntax--inherited-class {
  color: #98c379;
}
.syntax--keyword {
  color: #c678dd;
}
.syntax--keyword.syntax--control {
  color: #c678dd;
}
.syntax--keyword.syntax--operator {
  color: #abb2bf;
}
.syntax--keyword.syntax--other.syntax--special-method {
  color: #61afef;
}
.syntax--keyword.syntax--other.syntax--unit {
  color: #d19a66;
}
.syntax--storage {
  color: #c678dd;
}
.syntax--storage.syntax--type.syntax--annotation,
.syntax--storage.syntax--type.syntax--primitive {
  color: #c678dd;
}
.syntax--storage.syntax--modifier.syntax--package,
.syntax--storage.syntax--modifier.syntax--import {
  color: #abb2bf;
}
.syntax--constant {
  color: #d19a66;
}
.syntax--constant.syntax--variable {
  color: #d19a66;
}
.syntax--constant.syntax--character.syntax--escape {
  color: #56b6c2;
}
.syntax--constant.syntax--numeric {
  color: #d19a66;
}
.syntax--constant.syntax--other.syntax--color {
  color: #56b6c2;
}
.syntax--constant.syntax--other.syntax--symbol {
  color: #56b6c2;
}
.syntax--variable {
  color: #e06c75;
}
.syntax--variable.syntax--interpolation {
  color: #be5046;
}
.syntax--variable.syntax--parameter {
  color: #abb2bf;
}
.syntax--string {
  color: #98c379;
}
.syntax--string.syntax--regexp {
  color: #56b6c2;
}
.syntax--string.syntax--regexp .syntax--source.syntax--ruby.syntax--embedded {
  color: #e5c07b;
}
.syntax--string.syntax--other.syntax--link {
  color: #e06c75;
}
.syntax--punctuation.syntax--definition.syntax--comment {
  color: #5c6370;
}
.syntax--punctuation.syntax--definition.syntax--method-parameters,
.syntax--punctuation.syntax--definition.syntax--function-parameters,
.syntax--punctuation.syntax--definition.syntax--parameters,
.syntax--punctuation.syntax--definition.syntax--separator,
.syntax--punctuation.syntax--definition.syntax--seperator,
.syntax--punctuation.syntax--definition.syntax--array {
  color: #abb2bf;
}
.syntax--punctuation.syntax--definition.syntax--heading,
.syntax--punctuation.syntax--definition.syntax--identity {
  color: #61afef;
}
.syntax--punctuation.syntax--definition.syntax--bold {
  color: #e5c07b;
  font-weight: bold;
}
.syntax--punctuation.syntax--definition.syntax--italic {
  color: #c678dd;
  font-style: italic;
}
.syntax--punctuation.syntax--section.syntax--embedded {
  color: #be5046;
}
.syntax--punctuation.syntax--section.syntax--method,
.syntax--punctuation.syntax--section.syntax--class,
.syntax--punctuation.syntax--section.syntax--inner-class {
  color: #abb2bf;
}
.syntax--support.syntax--class {
  color: #e5c07b;
}
.syntax--support.syntax--type {
  color: #56b6c2;
}
.syntax--support.syntax--function {
  color: #56b6c2;
}
.syntax--support.syntax--function.syntax--any-method {
  color: #61afef;
}
.syntax--entity.syntax--name.syntax--function {
  color: #61afef;
}
.syntax--entity.syntax--name.syntax--class,
.syntax--entity.syntax--name.syntax--type.syntax--class {
  color: #e5c07b;
}
.syntax--entity.syntax--name.syntax--section {
  color: #61afef;
}
.syntax--entity.syntax--name.syntax--tag {
  color: #e06c75;
}
.syntax--entity.syntax--other.syntax--attribute-name {
  color: #d19a66;
}
.syntax--entity.syntax--other.syntax--attribute-name.syntax--id {
  color: #61afef;
}
.syntax--meta.syntax--class {
  color: #e5c07b;
}
.syntax--meta.syntax--class.syntax--body {
  color: #abb2bf;
}
.syntax--meta.syntax--method-call,
.syntax--meta.syntax--method {
  color: #abb2bf;
}
.syntax--meta.syntax--definition.syntax--variable {
  color: #e06c75;
}
.syntax--meta.syntax--link {
  color: #d19a66;
}
.syntax--meta.syntax--require {
  color: #61afef;
}
.syntax--meta.syntax--selector {
  color: #c678dd;
}
.syntax--meta.syntax--separator {
  background-color: #373b41;
  color: #abb2bf;
}
.syntax--meta.syntax--tag {
  color: #abb2bf;
}
.syntax--underline {
  text-decoration: underline;
}
.syntax--none {
  color: #abb2bf;
}
.syntax--invalid.syntax--deprecated {
  color: #523d14 !important;
  background-color: #e0c285 !important;
}
.syntax--invalid.syntax--illegal {
  color: #ffffff !important;
  background-color: #e05252 !important;
}
.syntax--markup.syntax--bold {
  color: #d19a66;
  font-weight: bold;
}
.syntax--markup.syntax--changed {
  color: #c678dd;
}
.syntax--markup.syntax--deleted {
  color: #e06c75;
}
.syntax--markup.syntax--italic {
  color: #c678dd;
  font-style: italic;
}
.syntax--markup.syntax--heading {
  color: #e06c75;
}
.syntax--markup.syntax--heading .syntax--punctuation.syntax--definition.syntax--heading {
  color: #61afef;
}
.syntax--markup.syntax--link {
  color: #c678dd;
}
.syntax--markup.syntax--inserted {
  color: #98c379;
}
.syntax--markup.syntax--quote {
  color: #d19a66;
}
.syntax--markup.syntax--raw {
  color: #98c379;
}
.syntax--source.syntax--c .syntax--keyword.syntax--operator {
  color: #c678dd;
}
.syntax--source.syntax--cpp .syntax--keyword.syntax--operator {
  color: #c678dd;
}
.syntax--source.syntax--cs .syntax--keyword.syntax--operator {
  color: #c678dd;
}
.syntax--source.syntax--css .syntax--property-name,
.syntax--source.syntax--css .syntax--property-value {
  color: #828997;
}
.syntax--source.syntax--css .syntax--property-name.syntax--support,
.syntax--source.syntax--css .syntax--property-value.syntax--support {
  color: #abb2bf;
}
.syntax--source.syntax--gfm .syntax--markup {
  -webkit-font-smoothing: auto;
}
.syntax--source.syntax--gfm .syntax--link .syntax--entity {
  color: #61afef;
}
.syntax--source.syntax--go .syntax--storage.syntax--type.syntax--string {
  color: #c678dd;
}
.syntax--source.syntax--ini .syntax--keyword.syntax--other.syntax--definition.syntax--ini {
  color: #e06c75;
}
.syntax--source.syntax--java .syntax--storage.syntax--modifier.syntax--import {
  color: #e5c07b;
}
.syntax--source.syntax--java .syntax--storage.syntax--type {
  color: #e5c07b;
}
.syntax--source.syntax--java .syntax--keyword.syntax--operator.syntax--instanceof {
  color: #c678dd;
}
.syntax--source.syntax--java-properties .syntax--meta.syntax--key-pair {
  color: #e06c75;
}
.syntax--source.syntax--java-properties .syntax--meta.syntax--key-pair > .syntax--punctuation {
  color: #abb2bf;
}
.syntax--source.syntax--js .syntax--keyword.syntax--operator {
  color: #56b6c2;
}
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--delete,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--in,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--of,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--instanceof,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--new,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--typeof,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--void {
  color: #c678dd;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--string.syntax--quoted.syntax--json {
  color: #e06c75;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation.syntax--string {
  color: #e06c75;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation {
  color: #98c379;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--constant.syntax--language.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--constant.syntax--language.syntax--json {
  color: #56b6c2;
}
.syntax--source.syntax--ruby .syntax--constant.syntax--other.syntax--symbol > .syntax--punctuation {
  color: inherit;
}
.syntax--source.syntax--python .syntax--keyword.syntax--operator.syntax--logical.syntax--python {
  color: #c678dd;
}
.syntax--source.syntax--python .syntax--variable.syntax--parameter {
  color: #d19a66;
}
</style>
  </head>
  <body class='markdown-preview' data-use-github-style><p>##Writeup Template</p>
<p>###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.</p>
<hr>
<p><strong>Vehicle Detection Project</strong></p>
<p>The goals / steps of this project are the following:</p>
<ul>
<li>Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier</li>
<li>Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.</li>
<li>Note: for those first two steps don&#39;t forget to normalize your features and randomize a selection for training and testing.</li>
<li>Implement a sliding-window technique and use your trained classifier to search for vehicles in images.</li>
<li>Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.</li>
<li>Estimate a bounding box for vehicles detected.</li>
</ul>
<h2 id="-rubric-https-review-udacity-com-rubrics-513-view-points"><a href="https://review.udacity.com/#!/rubrics/513/view">Rubric</a> Points</h2>
<h3 id="here-i-will-consider-the-rubric-points-individually-and-describe-how-i-addressed-each-point-in-my-implementation-">Here I will consider the rubric points individually and describe how I addressed each point in my implementation.</h3>
<hr>
<h3 id="histogram-of-oriented-gradients-hog-">Histogram of Oriented Gradients (HOG)</h3>
<h4 id="1-explain-how-and-identify-where-in-your-code-you-extracted-hog-features-from-the-training-images-">1. Explain how (and identify where in your code) you extracted HOG features from the training images.</h4>
<p>I extracted the HOG gradient using the code developed during the lessons.
For every image the scikit image library hog function is called.
In order to choose the parameter for the hog,(i.e. orient, pix_per_cell, cell_per_block)
I performed a grid search training several SVM classifier and choosing the one with the
best performance.
Here is an example using the <code>HLS</code> color space and HOG parameters of <code>orientations=9</code>, <code>pixels_per_cell=(8, 8)</code> and <code>cells_per_block=(2, 2)</code>:</p>
<p>Car image</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/1902.png" alt="alt text"></p>
<p>Hog feature for L channel of Car image</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/hog_1902.png" alt="alt text"></p>
<p>Non car image</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/extra1902.png" alt="alt text"></p>
<p>Hog feature for L channel of non car image</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/hog_extra1902.png" alt="alt text"></p>
<h4 id="2-explain-how-you-settled-on-your-final-choice-of-hog-parameters-">2. Explain how you settled on your final choice of HOG parameters.</h4>
<p>In order to decide which hog parameters works the best I decided to perfom a grid search
(the code for the grid search is in the <code>grid_search</code> function inside the <code>classifier.py</code> file
training different linear SVM classifier and the parameter that performed best were:</p>
<p><code>colorspace=YCrcb</code>
<code>orientation=9</code>
<code>pixels_per_cell=(8, 8)</code>
<code>cells_per_block=(2, 2)</code></p>
<h4 id="3-describe-how-and-identify-where-in-your-code-you-trained-a-classifier-using-your-selected-hog-features-and-color-features-if-you-used-them-">3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).</h4>
<p>I trained a linear SVM using the model selection function GridSearchCv provided
by the scikit learn library.
The tuned parameter was the C parameter of the classifier where I tried values 1, 10, 100.
In order to augment the data set used for the trained I used the udacity data set
cropping the car images following the annotation included and for every image in the training set I
filled it vertically in order to have a bigger training set.
Beside the udacity data set I used the KITTI_extracted dataset and the Extra data set as training set.</p>
<p>As a test set I used the GTI* data set.
Before training the classifier the number of car and non car examples were equalized for the training
set and the exceeding elements were added to the training set.</p>
<p>The grid search is in the <code>classify</code> function inside the <code>classifier.py</code> file.</p>
<h4 id="here-s-a-snippet-of-the-grid-search-output">Here&#39;s a snippet of the grid search output</h4>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Data&nbsp;summary:</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;11955&nbsp;&nbsp;not&nbsp;car&nbsp;images&nbsp;and&nbsp;&nbsp;11955&nbsp;&nbsp;car&nbsp;images&nbsp;and&nbsp;the&nbsp;ratio&nbsp;is&nbsp;&nbsp;1.0</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Testing&nbsp;set:&nbsp;We&nbsp;have&nbsp;&nbsp;5899&nbsp;&nbsp;not&nbsp;car&nbsp;images&nbsp;and&nbsp;&nbsp;5966&nbsp;&nbsp;car&nbsp;images&nbsp;and&nbsp;the&nbsp;ratio&nbsp;is&nbsp;&nbsp;0.988769694937982</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;colorspace:&nbsp;HLS&nbsp;&nbsp;orientations:&nbsp;9&nbsp;&nbsp;pixels&nbsp;per&nbsp;cell:&nbsp;8&nbsp;&nbsp;cell_per_block:&nbsp;2&nbsp;hog_channel:&nbsp;-1</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119:&nbsp;skimage_deprecation:&nbsp;Default&nbsp;value&nbsp;of&nbsp;`block_norm`==`L1`&nbsp;is&nbsp;deprecated&nbsp;and&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&#39;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15&#39;,&nbsp;skimage_deprecation)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>224.72&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;training&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>58.52&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;testing&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;47820&nbsp;&nbsp;training&nbsp;samples&nbsp;and&nbsp;train&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;11865&nbsp;&nbsp;test&nbsp;samples&nbsp;and&nbsp;test&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>After&nbsp;selecting&nbsp;feature&nbsp;we&nbsp;have&nbsp;&nbsp;(47820,&nbsp;1508)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Starting&nbsp;a&nbsp;SVM&nbsp;grid&nbsp;search</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>optimization&nbsp;finished,&nbsp;#iter&nbsp;=&nbsp;10000</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>WARNING:&nbsp;reaching&nbsp;max&nbsp;number&nbsp;of&nbsp;iterations</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;-s&nbsp;2&nbsp;may&nbsp;be&nbsp;faster&nbsp;(also&nbsp;see&nbsp;FAQ)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Objective&nbsp;value&nbsp;=&nbsp;-6084.402680</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>nSV&nbsp;=&nbsp;10936</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920:&nbsp;ConvergenceWarning:&nbsp;Liblinear&nbsp;failed&nbsp;to&nbsp;converge,&nbsp;increase&nbsp;the&nbsp;number&nbsp;of&nbsp;iterations.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&quot;the&nbsp;number&nbsp;of&nbsp;iterations.&quot;,&nbsp;ConvergenceWarning)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>[LibLinear]1556.2&nbsp;Seconds&nbsp;to&nbsp;Grid&nbsp;search&nbsp;SVC...</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Test&nbsp;Accuracy&nbsp;of&nbsp;SVC&nbsp;=&nbsp;&nbsp;0.8172&nbsp;&nbsp;f1&nbsp;score&nbsp;=&nbsp;&nbsp;0.8421&nbsp;&nbsp;precision&nbsp;=&nbsp;&nbsp;0.7444&nbsp;&nbsp;recall&nbsp;=&nbsp;&nbsp;0.9692</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;colorspace:&nbsp;YCrCb&nbsp;&nbsp;orientations:&nbsp;9&nbsp;&nbsp;pixels&nbsp;per&nbsp;cell:&nbsp;8&nbsp;&nbsp;cell_per_block:&nbsp;2&nbsp;hog_channel:&nbsp;-1</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119:&nbsp;skimage_deprecation:&nbsp;Default&nbsp;value&nbsp;of&nbsp;`block_norm`==`L1`&nbsp;is&nbsp;deprecated&nbsp;and&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&#39;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15&#39;,&nbsp;skimage_deprecation)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>815.79&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;training&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>228.78&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;testing&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;47820&nbsp;&nbsp;training&nbsp;samples&nbsp;and&nbsp;train&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;11865&nbsp;&nbsp;test&nbsp;samples&nbsp;and&nbsp;test&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>After&nbsp;selecting&nbsp;feature&nbsp;we&nbsp;have&nbsp;&nbsp;(47820,&nbsp;1609)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Starting&nbsp;a&nbsp;SVM&nbsp;grid&nbsp;search</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>optimization&nbsp;finished,&nbsp;#iter&nbsp;=&nbsp;10000</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>WARNING:&nbsp;reaching&nbsp;max&nbsp;number&nbsp;of&nbsp;iterations</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;-s&nbsp;2&nbsp;may&nbsp;be&nbsp;faster&nbsp;(also&nbsp;see&nbsp;FAQ)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Objective&nbsp;value&nbsp;=&nbsp;-5700.099888</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>nSV&nbsp;=&nbsp;10291</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920:&nbsp;ConvergenceWarning:&nbsp;Liblinear&nbsp;failed&nbsp;to&nbsp;converge,&nbsp;increase&nbsp;the&nbsp;number&nbsp;of&nbsp;iterations.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&quot;the&nbsp;number&nbsp;of&nbsp;iterations.&quot;,&nbsp;ConvergenceWarning)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>[LibLinear]1569.8&nbsp;Seconds&nbsp;to&nbsp;Grid&nbsp;search&nbsp;SVC...</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Test&nbsp;Accuracy&nbsp;of&nbsp;SVC&nbsp;=&nbsp;&nbsp;0.7388&nbsp;&nbsp;f1&nbsp;score&nbsp;=&nbsp;&nbsp;0.784&nbsp;&nbsp;precision&nbsp;=&nbsp;&nbsp;0.671&nbsp;&nbsp;recall&nbsp;=&nbsp;&nbsp;0.9428</span></span></span></div></pre><p>And so then I decided to use ONLY the GTI and KTTI data to fit the model
(also doing a grid search). I Always augmented the data using the flipping technique</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Data&nbsp;summary:</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;8968&nbsp;&nbsp;not&nbsp;car&nbsp;images&nbsp;and&nbsp;&nbsp;8792&nbsp;&nbsp;car&nbsp;images&nbsp;and&nbsp;the&nbsp;ratio&nbsp;is&nbsp;&nbsp;1.0200181983621475</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;colorspace:&nbsp;HLS&nbsp;&nbsp;orientations:&nbsp;9&nbsp;&nbsp;pixels&nbsp;per&nbsp;cell:&nbsp;8&nbsp;&nbsp;cell_per_block:&nbsp;2&nbsp;hog_channel:&nbsp;-1</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119:&nbsp;skimage_deprecation:&nbsp;Default&nbsp;value&nbsp;of&nbsp;`block_norm`==`L1`&nbsp;is&nbsp;deprecated&nbsp;and&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&#39;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15&#39;,&nbsp;skimage_deprecation)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>461.41&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;training&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;37296&nbsp;&nbsp;training&nbsp;samples&nbsp;and&nbsp;train&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;15984&nbsp;&nbsp;test&nbsp;samples&nbsp;and&nbsp;test&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>After&nbsp;selecting&nbsp;feature&nbsp;we&nbsp;have&nbsp;&nbsp;(37296,&nbsp;1303)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Starting&nbsp;a&nbsp;SVM&nbsp;grid&nbsp;search</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>optimization&nbsp;finished,&nbsp;#iter&nbsp;=&nbsp;10000</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>WARNING:&nbsp;reaching&nbsp;max&nbsp;number&nbsp;of&nbsp;iterations</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;-s&nbsp;2&nbsp;may&nbsp;be&nbsp;faster&nbsp;(also&nbsp;see&nbsp;FAQ)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Objective&nbsp;value&nbsp;=&nbsp;-374.613339</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>nSV&nbsp;=&nbsp;1324</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920:&nbsp;ConvergenceWarning:&nbsp;Liblinear&nbsp;failed&nbsp;to&nbsp;converge,&nbsp;increase&nbsp;the&nbsp;number&nbsp;of&nbsp;iterations.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&quot;the&nbsp;number&nbsp;of&nbsp;iterations.&quot;,&nbsp;ConvergenceWarning)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>[LibLinear]146.97&nbsp;Seconds&nbsp;to&nbsp;Grid&nbsp;search&nbsp;SVC...</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Test&nbsp;Accuracy&nbsp;of&nbsp;SVC&nbsp;=&nbsp;&nbsp;0.9746&nbsp;&nbsp;f1&nbsp;score&nbsp;=&nbsp;&nbsp;0.9743&nbsp;&nbsp;precision&nbsp;=&nbsp;&nbsp;0.9732&nbsp;&nbsp;recall&nbsp;=&nbsp;&nbsp;0.9754</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;colorspace:&nbsp;HSV&nbsp;&nbsp;orientations:&nbsp;9&nbsp;&nbsp;pixels&nbsp;per&nbsp;cell:&nbsp;8&nbsp;&nbsp;cell_per_block:&nbsp;2&nbsp;hog_channel:&nbsp;-1</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119:&nbsp;skimage_deprecation:&nbsp;Default&nbsp;value&nbsp;of&nbsp;`block_norm`==`L1`&nbsp;is&nbsp;deprecated&nbsp;and&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&#39;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15&#39;,&nbsp;skimage_deprecation)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>332.61&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;training&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;37296&nbsp;&nbsp;training&nbsp;samples&nbsp;and&nbsp;train&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;15984&nbsp;&nbsp;test&nbsp;samples&nbsp;and&nbsp;test&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>After&nbsp;selecting&nbsp;feature&nbsp;we&nbsp;have&nbsp;&nbsp;(37296,&nbsp;1351)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Starting&nbsp;a&nbsp;SVM&nbsp;grid&nbsp;search</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>optimization&nbsp;finished,&nbsp;#iter&nbsp;=&nbsp;10000</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>WARNING:&nbsp;reaching&nbsp;max&nbsp;number&nbsp;of&nbsp;iterations</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;-s&nbsp;2&nbsp;may&nbsp;be&nbsp;faster&nbsp;(also&nbsp;see&nbsp;FAQ)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Objective&nbsp;value&nbsp;=&nbsp;-121.404891</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>nSV&nbsp;=&nbsp;1175</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920:&nbsp;ConvergenceWarning:&nbsp;Liblinear&nbsp;failed&nbsp;to&nbsp;converge,&nbsp;increase&nbsp;the&nbsp;number&nbsp;of&nbsp;iterations.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&quot;the&nbsp;number&nbsp;of&nbsp;iterations.&quot;,&nbsp;ConvergenceWarning)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>[LibLinear]118.24&nbsp;Seconds&nbsp;to&nbsp;Grid&nbsp;search&nbsp;SVC...</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Test&nbsp;Accuracy&nbsp;of&nbsp;SVC&nbsp;=&nbsp;&nbsp;0.978&nbsp;&nbsp;f1&nbsp;score&nbsp;=&nbsp;&nbsp;0.9778&nbsp;&nbsp;precision&nbsp;=&nbsp;&nbsp;0.9806&nbsp;&nbsp;recall&nbsp;=&nbsp;&nbsp;0.975</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;colorspace:&nbsp;YCrCb&nbsp;&nbsp;orientations:&nbsp;9&nbsp;&nbsp;pixels&nbsp;per&nbsp;cell:&nbsp;8&nbsp;&nbsp;cell_per_block:&nbsp;2&nbsp;hog_channel:&nbsp;-1</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119:&nbsp;skimage_deprecation:&nbsp;Default&nbsp;value&nbsp;of&nbsp;`block_norm`==`L1`&nbsp;is&nbsp;deprecated&nbsp;and&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&#39;be&nbsp;changed&nbsp;to&nbsp;`L2-Hys`&nbsp;in&nbsp;v0.15&#39;,&nbsp;skimage_deprecation)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>661.23&nbsp;Seconds&nbsp;to&nbsp;extract&nbsp;HOG&nbsp;features...for&nbsp;training&nbsp;set</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;37296&nbsp;&nbsp;training&nbsp;samples&nbsp;and&nbsp;train&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>We&nbsp;have&nbsp;&nbsp;15984&nbsp;&nbsp;test&nbsp;samples&nbsp;and&nbsp;test&nbsp;Feature&nbsp;vector&nbsp;length:&nbsp;8460</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>After&nbsp;selecting&nbsp;feature&nbsp;we&nbsp;have&nbsp;&nbsp;(37296,&nbsp;1363)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Starting&nbsp;a&nbsp;SVM&nbsp;grid&nbsp;search</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................*........................................................................................................................................</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>optimization&nbsp;finished,&nbsp;#iter&nbsp;=&nbsp;10000</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>WARNING:&nbsp;reaching&nbsp;max&nbsp;number&nbsp;of&nbsp;iterations</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Using&nbsp;-s&nbsp;2&nbsp;may&nbsp;be&nbsp;faster&nbsp;(also&nbsp;see&nbsp;FAQ)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;</span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Objective&nbsp;value&nbsp;=&nbsp;-53.637501</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>nSV&nbsp;=&nbsp;999</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>/usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920:&nbsp;ConvergenceWarning:&nbsp;Liblinear&nbsp;failed&nbsp;to&nbsp;converge,&nbsp;increase&nbsp;the&nbsp;number&nbsp;of&nbsp;iterations.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>&quot;the&nbsp;number&nbsp;of&nbsp;iterations.&quot;,&nbsp;ConvergenceWarning)</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>[LibLinear]98.87&nbsp;Seconds&nbsp;to&nbsp;Grid&nbsp;search&nbsp;SVC...</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>Test&nbsp;Accuracy&nbsp;of&nbsp;SVC&nbsp;=&nbsp;&nbsp;0.983&nbsp;&nbsp;f1&nbsp;score&nbsp;=&nbsp;&nbsp;0.9829&nbsp;&nbsp;precision&nbsp;=&nbsp;&nbsp;0.9844&nbsp;&nbsp;recall&nbsp;=&nbsp;&nbsp;0.9815</span></span></span></div></pre><h3 id="snippet-of-the-used-data-and-grid-search">Snippet of the used data and grid Search</h3>
<p>In order to reduce the number of feature a feature selection was performed
training a forest of decision tree and then filtering the features using the
feature<em>importances</em> parameter of the ExtraTreesClassifier provided by scikit-learn
The feature selection code is inside <code>classify</code> function. I selected the feature
whose importance is bigger then the average value of the importances</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/feature_importances_2.png" alt="alt text"></p>
<p>So I reduced the number of feature used, speeding up the classifier without
loosing much in accuracy</p>
<h3 id="sliding-window-search">Sliding Window Search</h3>
<h4 id="1-describe-how-and-identify-where-in-your-code-you-implemented-a-sliding-window-search-how-did-you-decide-what-scales-to-search-and-how-much-to-overlap-windows-">1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?</h4>
<p>The sliding window implementation is the one found during the lesson.
The scale and the overlap was decided extracting some frames from the test_video
and trying to identify cars in there.
I also reduced the space where the image is searched as is useless to search for
cars in the sky or over the horizon line.</p>
<p>Search area</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/search_area.png" alt="alt text"></p>
<h4 id="2-show-some-examples-of-test-images-to-demonstrate-how-your-pipeline-is-working-what-did-you-do-to-optimize-the-performance-of-your-classifier-">2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?</h4>
<p>I searched on two scales using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result even if
some false positives are still present. Probably doing more grid search and selecting better training and test frame can lead to better performances.</p>
<p>Here are some example images:</p>
<p>Detected cars (with false positive)</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/detected.png" alt="alt text"></p>
<p>Detected cars</p>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/detected_2.png" alt="alt text"></p>
<hr>
<h3 id="video-implementation">Video Implementation</h3>
<h4 id="1-provide-a-link-to-your-final-video-output-your-pipeline-should-perform-reasonably-well-on-the-entire-project-video-somewhat-wobbly-or-unstable-bounding-boxes-are-ok-as-long-as-you-are-identifying-the-vehicles-most-of-the-time-with-minimal-false-positives-">1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)</h4>
<p>Here&#39;s a <a href="./project_video.mp4">link to my video result</a></p>
<h4 id="2-describe-how-and-identify-where-in-your-code-you-implemented-some-kind-of-filter-for-false-positives-and-some-method-for-combining-overlapping-bounding-boxes-">2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.</h4>
<p>I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used <code>scipy.ndimage.measurements.label()</code> to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.<br>I integrated the last 10 heatmaps keeping them in a circular buffer. These maps are summed and then thresholded in order to keep points that continue to have a positive match throughout different frames.
This prevent frame to disappear in 10 frames :)</p>
<p>Here&#39;s an example result showing the heatmap from a series of frames of video, the result of <code>scipy.ndimage.measurements.label()</code> and the bounding boxes then overlaid on the last frame of video:</p>
<h3 id="here-some-frames-and-their-corresponding-heatmaps-">Here some frames and their corresponding heatmaps:</h3>
<h4 id="frame-1">Frame 1</h4>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/detected.png" alt="alt text">
<img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/heatmap.png" alt="alt text"></p>
<h4 id="frame-2">Frame 2</h4>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/detected_2.png" alt="alt text">
<img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/heatmap_2.png" alt="alt text"></p>
<h3 id="here-is-the-output-of-scipy-ndimage-measurements-label-on-the-integrated-heatmap-from-previous-frames-">Here is the output of <code>scipy.ndimage.measurements.label()</code> on the integrated heatmap from previous frames:</h3>
<h4 id="integrated-heatmap">Integrated heatmap</h4>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/total_heatmap.png" alt="alt text"></p>
<h3 id="here-the-resulting-bounding-boxes-are-drawn-onto-the-last-frame-in-the-series-">Here the resulting bounding boxes are drawn onto the last frame in the series:</h3>
<p><img src="/home/seba/Projects/Courses/self_driving_car/assigments/CarND-Vehicle-Detection/output_images/result.png" alt="alt text"></p>
<hr>
<h3 id="discussion">Discussion</h3>
<h4 id="1-briefly-discuss-any-problems-issues-you-faced-in-your-implementation-of-this-project-where-will-your-pipeline-likely-fail-what-could-you-do-to-make-it-more-robust-">1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?</h4>
<p>My implemntation is far from be perfect.
Sometimes cars are not detected and still lots of false positive are present.
I think the classifier is still the weakest point in this implementation.</p>
<ul>
<li>Lot of work can be done to increase the performances. (grid search, augment dataset,
get rid of fimeframes inside the current dataset)</li>
<li>More work can also be done on the bounding boxes in order to better fit the
corrisponding detected object.</li>
<li>Speed also is a problem...but with a more precise classifier the overlap between
windows can be increased hence resulting in less windows to search and more speed.</li>
<li>I could not succeeded in fitting a model using also udacity data...
model accuracy was always too low and lot of false negatives..so probably in
this case is better a model that overfits a bit and then using filtering
of false positives a lot</li>
</ul></body>
</html>
