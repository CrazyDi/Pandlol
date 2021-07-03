import React from 'react'
import Label from 'controls/Label'
import ISearchResultItem from 'app/interfaces/ISearchResultItem'
import HomePageSearchResultItem from './Item'
import useStyles from './styles'

interface Props {
    items: ISearchResultItem[]
}

const HomePageSearchResult = (props: Props) => {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <div>
                <Label>Search Results:</Label>
                {props.items.length === 0 &&
                    <Label>No items found</Label>
                }
                {props.items.length > 0 &&
                    props.items.map((item) =>
                        <HomePageSearchResultItem item={item}/>
                    )
                }
            </div>
        </div>
    )
}

export default HomePageSearchResult
