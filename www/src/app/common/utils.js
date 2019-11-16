const utils = {};

utils.getClassName = (...args) => {
    let classNames = [];

    for (let i = 0; i < args.length; i++) {
        let arg = args[i];

        if (arg) {
            if (Array.isArray(arg)) {
                if (arg[1]) {
                    classNames.push(arg[0]);
                }
            } else {
                classNames.push(arg);
            }
        }
    }

    return classNames.join(' ');
};

export default utils;
