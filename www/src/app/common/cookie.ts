interface ICookieOptions {
    expires?: string | number | Date
    [property: string]: any
}

const getValue = (key: string) => {
    let cookieValue

    const matches = document.cookie.match(new RegExp(
        `(?:^|; )${key.replace(/([.$?*|{}()[]\/+^])/g, '\\$1')}=([^;]*)`
    ))

    if (matches && matches.length > 1) {
        cookieValue = decodeURIComponent(matches[1])
    }

    return cookieValue
}

const setValue = (key: string, value: string, options: ICookieOptions) => {
    const cookieOptions: ICookieOptions = {
        path: '/',
        ...options
    }

    if (cookieOptions.expires instanceof Date) {
        cookieOptions.expires = cookieOptions.expires.toUTCString()
    }

    let updatedCookie = `${encodeURIComponent(key)}=${encodeURIComponent(value)}`

    Object.keys(cookieOptions).forEach((key) => {
        const optionValue = cookieOptions[key]

        updatedCookie += `; ${key}`

        if (optionValue !== true) {
            updatedCookie += `=${optionValue}`
        }
    })

    document.cookie = updatedCookie
}

const deleteKey = (key: string) => {
    setValue(key, '', {
        'max-age': -1
    })
}

export default {
    getValue,
    setValue,
    deleteKey
}
