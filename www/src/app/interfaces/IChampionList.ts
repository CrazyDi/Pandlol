import IChampion from './IChampion'

export default interface IChampionList {
    items: IChampion[]
    total: number
}

export const parseChampionList = (data: { [property: string]: any }): IChampionList => {
    const championList: IChampionList = {
        items: [],
        total: data.total
    }

    return championList
}
