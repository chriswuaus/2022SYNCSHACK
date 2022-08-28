export type UnitCardProps = {
  unitCode: string;
  unitName: string;
  unitRating: number;
};

export type SideBarProps = {};

export type ButtProps = {
  highlighted: boolean;
  link: string;
};

export type SearchProps = {
  highlighted: boolean;
  link: string;
};

export type DegreeProps = {
  degreeName: string;
  degreeYear: number;
  semester: number;
  major: string;
  link: string;
};

export type DegreeEntryProps = {
  onAdd: (degree: DegreeProps) => void
}

export type SemesterBlockProps = {
  cards: UnitCardProps[];
};

export type UnitEntryProps = {
  subjects: Array<string>;
};
