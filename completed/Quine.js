function quine(b) {const s = '`function quine(b) {const s = ${String.fromCharCode(39)}${s}${String.fromCharCode(39)};if(b) return s;return ${quine(true)};}`';if(b) return s;return `function quine(b) {const s = ${String.fromCharCode(39)}${s}${String.fromCharCode(39)};if(b) return s;return ${quine(true)};}`;}