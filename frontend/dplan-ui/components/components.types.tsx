export type UnitCardProps = {
  unitCode: string;
  unitName: string;
  unitRating: number;
};

export type SideBarProps = {
}

export type SemesterBlockProps = {
  cards: UnitCardProps[];
}
