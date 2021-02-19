import React, { useContext, useState } from 'react'
import clsx from 'clsx'

import useStyles from './styles'

interface Props {
    className?: string
    disabled?: boolean
    checkedValue?: string
    children?: React.ReactNode
}

export interface IRadioButtonsContext {
    checkedValue?: string
    onCheckedValueChanged: (checkedValue: string) => void
}

const radioButtonsContext: IRadioButtonsContext = {
    checkedValue: undefined,
    onCheckedValueChanged: () => {}
}

export const RadioButtonsContext = React.createContext(radioButtonsContext)

const RadioButtons = (props: Props) => {
    const [checkedValue, setCheckedValue] = useState<string|undefined>(props.checkedValue)

    const classes = useStyles({
        disabled: props.disabled
    })

    const className = clsx(classes.component, props.className)
    const attributes: { [index: string]: any } = {}

    if (props.disabled) {
        attributes['aria-disabled'] = true
        attributes.disabled = true
    }

    const radioButtonsContextProviderValue: IRadioButtonsContext = {
        checkedValue: checkedValue,
        onCheckedValueChanged: (checkedValue) => {
            setCheckedValue(checkedValue)
        }
    }

    return (
        <div
            {...attributes}
            className={className}
        >
            <RadioButtonsContext.Provider value={radioButtonsContextProviderValue}>
                {props.children}
            </RadioButtonsContext.Provider>
        </div>
    )
}

export default RadioButtons
